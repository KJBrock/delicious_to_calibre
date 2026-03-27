

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
    
