#from calibre import db
import csv

#db = db('/Users/kevinbrock/Documents/Calibre/Main').new_api

catalog_entries = []
with open("../catalog20260322.as_csv.csv", newline='') as catalog:
    catalog_reader = csv.reader(catalog, delimiter=',', quotechar='"')
    for entry in catalog_reader:
        catalog_entries.append(entry)

field_names = catalog_entries[0]
book_entries = catalog_entries[1:]

books = {}
for book_entry in book_entries:
    book = dict(zip(field_names, book_entry))
    books.append(book)
    
    
    