import csv
import subprocess
from constants import *
from conversion_mapping import *
from arguments import retrieve_arguments
from delicious import import_from_delicious_csv
from calibre import *

def main():        
    
    args = retrieve_arguments()

    create_custom_columns(custom_columns, 
                          args.calibre_library_location)

    books = import_from_delicious_csv(args.library_file)
    
    #test_books = books[2010:2040]
    
    print("Adding books to calibre...")
    add_books_to_calibre(test_books, args.calibre_library_location)
    
    print("Setting extra book data...")
    for book in test_books:
        if "calibre_id" in book:
            print(f"Adding extra data for {book["title"]} -- {book["creator"]}")
            add_book_format(book, args.calibre_library_location)
        else:
            print(f"Item not added to calibre: {book["title"]}")

        for k in book:
            if len(k) == 0:
                continue
            
            field_name = get_mapped_field(k, args.calibre_library_location)
            
            # Set custom values
            if field_name in custom_columns.keys():
                set_column_data(book, k, field_name, ["is_multiple"], args.calibre_library_location)
                continue       

            # Set metadata
            if is_metadata_field(k, args.calibre_library_location):
                field_name = get_mapped_field(k, args.calibre_library_location)
                set_metadata(field_name, book[k], book["calibre_id"], args.calibre_library_location)
        
if __name__ == "__main__":
    main()
    
