import csv

def import_from_delicious_csv(library_file):        
    
    catalog_entries = []
    with open(library_file, newline='') as catalog:
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

    return books


