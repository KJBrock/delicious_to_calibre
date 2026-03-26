import csv
import subprocess
import argparse

# We don't ever need to read this file.  It's consumed by calibre.  We just need to write out all of
# the physical book specific info.  The available lib, tomllib is read-only.  It's a simple enough 
# file in our case that we'll just write it by hand.
#
def write_toml_data(book, filename):
    # Not actually writing to the file yet
    # with open(filename, "w") as tomlfile:
    print("[metadata]")
        # author
        # title
        # pages
        # location
        # shelves
        # binding
    
def main():        
    parser = argparse.ArgumentParser()
    parser.parse_args()

    # These are usable only from the Calibre dev environment.  If I make a Calibre plugin 
    # maybe they'll be useful...

    #from calibre import db
    #db = db('/Users/kevinbrock/Documents/Calibre/Main').new_api

    catalog_entries = []
    with open("../catalog20260322.as_csv.csv", newline='') as catalog:
        catalog_reader = csv.reader(catalog, delimiter=',', quotechar='"')
        for entry in catalog_reader:
            catalog_entries.append(entry)

    # first line of the csv file is column headers.
    field_names = catalog_entries[0]
    # The rest are book/DVD/VHS/CD entries.
    book_entries = catalog_entries[1:]
        
    # This will give us an array of ~11000 books with the catalog above.
    #
    books = [dict(zip(field_names, book_entry)) for book_entry in book_entries]   


    # maybe use subprocess + calibredb to add books to the database?  Need to test this pretty
    # thoroughly with a test database before touching the real thing.
    #

if __name__ == "__main__":
    main()
    
