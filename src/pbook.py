import os

# We don't ever need to read the pbook file.  It's consumed by calibre.  We just need to write out all of
# the physical book specific info.  The available lib, tomllib is read-only.  It's a simple enough 
# file in our case that we'll just write it by hand.
#
def write_pbook_data(book, filename):
    with open(filename, "w") as tomlfile:
        tomlfile.write("[metadata]\n\n")
        if "creator" in book:            
            tomlfile.write(f"author={book["creator"]}\n")
        else:
            tomlfile.write(f"author=unknown\n")
            
        if "title" in book:
            tomlfile.write(f"title={book["title"]}\n")
        else:
            tomlfile.write(f"title=unknown\n")
            
        if "location" in book:
            tomlfile.write(f"location={book["location"]}\n")
        if "shelves" in book:
            tomlfile.write(f"shelves={book["shelves"]}\n")
        if "library of congress" in book:
            tomlfile.write(f"library_of_congress={book["library of congress"]}\n")
        if "isbn" in book:
            tomlfile.write(f"ISBN={book["isbn"]}\n")
        if "pages" in book:
            tomlfile.write(f"pages={book["pages"]}\n")

        tomlfile.write("\n[original data]\n\n")
        tomlfile.write(f"{book}\n")

def clean_up_pbook(filename):
    try:
        os.remove(filename)
    except OSError as err:
        print(f"Error removing file {filename}: {err}")
        
        
        