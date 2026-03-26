# calibredb

## Adding Files

The basic add command for calibredb looks like this:

```    
calibredb --with-library <library location> add --authors "an author" --title "a title" --empty
```

The problem is how we get the book back later to use things like add_format.  The other calibredb functions which operate on a book take the book ID as an argument.  The solution to that is a bit weird.  You don't get back any information on what you just added, so you need to do a search.  In the test case this is easy, but in the _real_ book database there are duplicates both in the library and the calibre databases.

Using the `--tags` option seems like a simple way to do it. 

1. Genereate a UUID for the book we're about to add.
2. Set that UUID as a tag in the add command

```    
calibredb --with-library <library location> add --authors "an author" --title "a title" --tags <UUID> --empty
```

3. Search for that tag.  We should get back exactly one value, which is the ID of the book.

```
calibredb search "tags:<UUID>" --library-path <library location>
```

4. Use that ID for anything else we need to set.  At a minimum this will include adding a format, e.g.

```
calibredb --with-library <library location> add_format <ID> <book title>.pbook
```

Where the pbook file is physical-book-specific information.

## More to look at

- `add_custom_column`
- `set_custom`
- `set_metadata` Need to verify how this interacts with the `[metadata]` section in the .pbook file.  Is that read when the book format is added?  I cna check that with `show_metadata` after the initial add process is finished.
- `backup_metadata` This normally happens automatically, but can be forces with `--all`
