import subprocess
import re
from pbook import write_pbook_data, clean_up_pbook
from constants import *
from conversion_mapping import *

def is_metadata_field(field_name, calibre_library):
    if field_name in field_name_mapping and field_name_mapping[field_name] in metatdata_fields:
        return True
    return False

def get_mapped_field(field_name, calibre_library):
    if field_name in field_name_mapping:
        return field_name_mapping[field_name]
    return field_name

def set_metadata(field_name, value, book_id, calibre_library):
    command = ["calibredb", "--with-library", f"{calibre_library}", "set_metadata"]
    command.append("--field")
    command.append(f"{field_name}:{value}")
    command.append(f"{book_id}")
    #print(f"Setting metadata: {" ".join(command)}")
    set_metadata_result = subprocess.run(command, capture_output=True, text=True)
    if set_metadata_result.returncode != 0: # It failed
        print(f"Set metadata {field_name} failed.")
        return
    
def get_custom_colums(calibre_library):
    command = ["calibredb", "--with-library", f"{calibre_library}", "custom_columns"]
    get_columns_result = subprocess.run(command, capture_output=True, text=True)

    #print(f"Columns result: {get_columns_result.returncode}, stdout: {get_columns_result.stdout} stderr: {get_columns_result.stderr}")
    if get_columns_result.returncode != 0: # It failed
        print(f"Columns result: {get_columns_result.returncode}, stdout: {get_columns_result.stdout} stderr: {get_columns_result.stderr}")
        exit(1)

    if len(get_columns_result.stdout) == 0:    
        # print("No custom columns in database.")
        return set()
    
    column_list = get_columns_result.stdout.split("\n")
    column_list = [item.split(" ")[0] for item in column_list if len(item) > 0]
    return set(column_list)

def set_column_data(book, original_field, column_name, is_multiple, calibre_library):
    command = ["calibredb", "--with-library", f"{calibre_library}", "set_custom"]
    if is_multiple:
        command.append("--append")
    command.append(f"{column_name}")
    command.append(f"{book["calibre_id"]}")

    if is_multiple:
        value_list = book[original_field].split(",")
        value_list = [v.strip() for v in value_list]
        # print(f"Initial value list: {value_list}")
        for v in value_list:
            item_command = command.copy()
            item_command.append(v)
            set_column_result = subprocess.run(item_command, capture_output=True, text=True)
            if set_column_result.returncode != 0: # It failed
                print(f"Set custom column value (multiple) failed for {column_name}, {v}.")
                return

    else:
        command.append(book[original_field]) 
        set_column_result = subprocess.run(command, capture_output=True, text=True)
        if set_column_result.returncode != 0: # It failed
            print(f"Set custom column value failed for {column_name}, {book[original_field]}")
            return

def get_column_description(enum_values):
    values = ", ".join([f"\"{v}\"" for v in enum_values])
    description_params = f"{{\"enum_values\": [{values}], \"enum_colors\": [], \"use_decorations\": false, \"description\": \"\", \"web_search_template\": \"\"}}"
    # print(description_params)
    return description_params
    
# Columns: 
#    name: { "friendly" : <friendly name>,
#            "type" : <column type>,
#            "is_multiple": bool }
#
def create_custom_columns(columns, calibre_library):
    new_columns = set(columns.keys())
    old_columns = get_custom_colums(calibre_library)
    need_columns = new_columns - old_columns

    for column in need_columns:
        # print(f"Checking {column}")
        command = ["calibredb", "--with-library", f"{calibre_library}", "add_custom_column"]
        if columns[column]["is_multiple"] == True:
            command.append("--is-multiple")       
            
        if columns[column]["type"] == "enumeration":
            command.append("--display") 
            column_description = get_column_description(columns[column]["enum_values"])
            command.append(column_description)

        command.append(column)
        command.append(columns[column]["friendly"])
        command.append(columns[column]["type"])
        add_column_result = subprocess.run(command, capture_output=True, text=True)
        if add_column_result.returncode != 0: # It failed
            print(f"Add column failed: {add_column_result.returncode}, stdout: {add_column_result.stdout} stderr: {add_column_result.stderr}")
            return
        
        # print(f"Add column ok: {add_column_result.returncode}, stdout: {add_column_result.stdout} stderr: {add_column_result.stderr}")
                
    
# Adds books to the calibre database
# 
# Modifies book dict to contain UUID used for locating it within calibre, as well as "official" calibre ID
#
def add_books_to_calibre(books, calibre_library):
    print(f"Adding {len(books)} books to calibre")
    for book in books:        
        command = ["calibredb", "--with-library", f"{calibre_library}", "add", "--duplicates"]

        if len(book["creator"]) > 0:
            command.append("--authors")
            command.append(f"{book["creator"]}")

        if len(book["title"]) > 0:
            command.append("--title")
            command.append(f"{book["title"]}")
    
        if book["ISBN"] != "":
            command.append("--identifier")
            command.append(f"isbn:{book["ISBN"]}")
            
        if len(book["series"]) > 0:
            command.append("--series")
            command.append(f"{book["series"]}")
            series_index = int(book["no. in series"])
            if series_index > 0:
                command.append("--series-index")
                command.append(f"{series_index}")
        
        if "your image URL" in book and len(book["your image URL"]) > 0:
            command.append("--cover")
            command.append(book["your image URL"])

        command.append("--empty")
        
        print(f"Adding item: {book["title"]} -- {book["creator"]}")            

        add_result = subprocess.run(command, capture_output=True, text=True)
        if add_result.returncode != 0: # It worked
            print(f"Add failed: {add_result.returncode}, stdout: {add_result.stdout} stderr: {add_result.stderr}")
            return

        match = re.match(BOOK_ID_REGEX, add_result.stdout)
        if match != None:
            calibre_id = int(match.group(1))
        book["calibre_id"] = calibre_id
                
        

def add_book_format(book, calibre_library):

    command = ["calibredb", "--with-library", f"{calibre_library}", "add_format", f"{book["calibre_id"]}"]
    
    pbook_file_name = f"{book["title"]}.pbook"
    write_pbook_data(book, pbook_file_name)

    command.append(pbook_file_name)
    format_result = subprocess.run(command, capture_output=True, text=True)
    if format_result.returncode != 0:
        print(f"Error adding format: {format_result.returncode}, stdout: {format_result.stdout} stderr: {format_result.stderr}")
    
    clean_up_pbook(pbook_file_name)
