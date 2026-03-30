# This information is pretty specific to my library.  I'll be using it to try to consolidate
# fields that are saying the same thing with different words.
#
media_types = [
    "Music",
    "Book",
    "Toy",
    "Movie",
]

custom_columns = {  "shelves" : {"friendly" : "Shelves",
                                "type" : "text",
                                "is_multiple" : True },
                  
                    "location" : {"friendly" : "Location",
                                  "type" : "text",
                                  "is_multiple" : False},
                    
                    "itemtype" : {"friendly" : "Item Type",
                                  "type" : "enumeration",
                                  "is_multiple" : False,
                                  "enum_values" : media_types},
                    
                    "media_languages" : {"friendly" : "Media Languages",
                                "type" : "text",
                                "is_multiple" : True },
                  
                    }
            
# These are also metadata fields, but we're setting them during add:
#
#                    "title" : "Title",  # This is being set in add item                                   
#                    "authors" : "Authors", # This is being set in add item
#                    "identifiers" : "Identifiers", # This is being set in add item               
#                    "series" : "Series",  # This is being set in add item                                  
#                    "series_index" : "Series Index",  # This is being set in add item                            
#                    "cover" : "Cover",                                   
metatdata_fields = {"#chronology" : "Internal Chronology",                       
                    "#course" : "Course",                                   
                    "#edited" : "Ed",                                       
                    "#readinglist" : "ReadingList",                              
                    "#sequelto" : "Sequel To",                                
                    "author_sort" : "Author sort",                              
                    "comments" : "Comments",                                 
                    "id" : "Id",                                       
                    "languages" : "Languages",                                
                    "pubdate" : "Published",                                
                    "publisher" : "Publisher",                                
                    "rating" : "Rating",                                   
                    "size" : "Size",                                     
                    "sort" : "Title sort",                               
                    "tags" : "Tags",                                     
                    "timestamp" : "Date",}                                    

# Delicious Library : Calibre
field_name_mapping = {
    # These first few fields we're changing the names to fit with calibre (or work aruond calibre)
    "creator" : "author", # modified.  It can have multiple authors, just space separated.  Needs to be checked by hand :-(
    "item type" : "itemtype",
    "no. in series" : "series_index",
    "release date" : "pubdate",
    "ISBN" : "isbn", # modified
#    "languages" : "languages", # Calibre expects a specific set of language abbreviations (ISO639)
    "languages" : "media_languages", # So we're going to create a custom column
    "your image URL" : "cover",

    "title" : "title",
    "format" : "format",
    "series" : "series",
    "publisher" : "publisher",
    "purchase date" : "purchase date",
    "creation date" : "creation date",
    "library of congress" : "library of congress",
    "location" : "location",
    "shelves" : "shelves", # this is a list of shelves (in Library) which show the item.  Comma separated.
    "amazon link" : "amazon link",
    "amazon product group" : "amazon product group",
    "audience" : "audience",
    "cinematographer" : "cinematographer",
    "composer" : "composer",
    "condition" : "condition", # unused
    "conductor" : "conductor",
    "country" : "country",
    "cover color" : "cover color",
    "current value" : "current value",
    "dewey decimal" : "dewey decimal",
    "EAN" : "EAN",
    "edition" : "edition",
    "features" : "features",
    "genres" : "genres",
    "height" : "height",
    "illustrator" : "illustrator",
    "key" : "key", #unused
    "length" : "length",
    "maximum players" : "maximum players",
    "minimum players" : "minimum players",
    "net rating" : "net rating",
    "no. of items" : "no. of items",
    "notes" : "notes",
    "owner" : "owner", # unused
    "pages" : "pages",
    "platform" : "platform",
    "played / read" : "played / read",
    "primary synopsis" : "primary synopsis",
    "private" : "private",
    "purchase price" : "purchase price",
    "rare" : "rare",
    "rating" : "rating",
    "retail price" : "retail price",
    "running time" : "running time",
    "screenwriter" : "screenwriter", # unused
    "serial number" : "serial number",
    "signed" : "signed",
    "stars" : "stars",
    "subtitle" : "subtitle",
    "theatrical debut" : "theatrical debut",
    "tracks" : "tracks",
    "unique item key" : "unique item key",
    "url" : "url", # unused
    "used" : "used",
    "weight" : "weight",
    "width" : "width",
}

# These all mean pretty much the same thing.
format_audio_cd_set = {
    "Audio CD",
    "CD from UK Import",
    "Audio CD Soundtrack",
    "Audio CD Cast Recording",
    "Audio CD Live",
    "CD audio Bande originale Import",
    "CD",
    "Audio CD Enhanced Original recording remastered",
    "Audio CD Explicit Lyrics Extra tracks",
    "Audio CD Import Live",
    "Audio CD Box set",
    "Audio CD Import",
    "Audio CD Enhanced",
    "Audio CD Explicit Lyrics",
    "Audio CD Import Cast Recording",
    "CD audio Import",
    "Audio CD Original recording remastered",    
}

# These all mean pretty much the same thing.
format_audio_cassette_set = {
    "Audio Cassette Audiobook",
    "Cassette",
    "Audio Cassette",
    "Tape",
    "Casette Tape",
}

formats = [
    "DVD-ROM",
    "DVD",
    "VHS",
    "VHS Tape",
    "Blu-ray",

    "Mass Market Paperback",
    "Mass Market Paperback Illustrated",

    "Perfect Paperback",

    "Paperback Abridged",
    "Paper",
    "Paperback Illustrated",
    "Paperback",
    "Paperbackl",
    "Paperback Box set",
    "Paperback Unabridged",
    "Paperback CD-ROM",
    "Paperback Facsimile",
    "paperback",

    "Trade Paper",
    "Trade Paperback",

    "Black Leather",
    "Leather 4to",
    "Leather Bound",
    "Leatherbound",
    "Leather",

    "Spiral Bound",
    "Spiral-bound",

    "Hardback",
    "Hardbound",
    "Hardcover Abridged",
    "Hardcover Unabridged",
    "Hardcover CD-ROM",
    "Hardcover Illustrated",
    "Hardcover",
    "Clothbound",

    "Library",
    "Library Binding",
    "School & Library Binding",

    "Board book",
    "Board book Unabridged",

    "Textbook Binding",
    "Toy",
    "Kindle Edition",

    "Unbekannter Einband",
    "Map",
    "Software",
    "Turtleback",
    "Plastic Comb",
    "Unknown Binding",
    "Relié",
    "Comic",
    "Broché",
    "Roughcut",
    "Loose Leaf",
    "Poche",
    "Ring Binder",
    "Binder",
    "Magazine",
    "4to",
    "Audio CD Audiobook",
    "Unbound",
    "Photocopy",
    "Cards",
]