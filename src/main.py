import csv
import subprocess
from constants import *
from arguments import retrieve_arguments
from pbook import write_toml_data

def main():        
    
    args = retrieve_arguments()

    catalog_entries = []
    with open(args.library_file, newline='') as catalog:
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
    
