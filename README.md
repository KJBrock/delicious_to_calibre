# Delicious to Calibre

## What?

The intent of this project is to convert a database (or export) of Delicious Library<sup>**2**</sup> books to a format acceptable by Calibre, and to add them to a Calibre library.  There are several ways to do this, and I'll be starting with (what I think of) as one of the simplest.

## Why?

Delicious Library was a wonderful app on macOS which tracked your physical books, and included support for both entering book data _via_ an iOS scanning app and looking up book information automatically on Amazon.

Sadly it is no more<sup>**3**</sup><sup>**4**</sup>.  A change in Amazon's fee structure for querying book data made it impractical for the authors to continue without a aubscription-based app, and so they let the project drop.

Now I have many thousands of book entries in a no longer supported app.  So...

## How?

Well, this _should_ be relatively straightforward, 

1. Look at the files exported by Library, and import them into Python.  This is easy to do using CSV export from Library and import into Python.  We end up with a very large array of dictionaries.

2. Use the `calibredb` command line app with Python's `subproces` module to manipulate the library.

3. Map the information organization in Library to the information organization in Calibre for information common to both.  For example, Calibre says "authors", Library says "creator".

4. Create meta-data for new media types.  There is some information available on parts of the problem<sup>**5**</sup><sup>**6**</sup>. Library supports physical books in multiple types of covers, DVDs, CDs and VHS.

## Current Status

Right now it handles basic import, re-creating Shelves, Media Type.  The following two items are ones I plan to get around to soon.

- I haven't had any luck getting calibre to automatically grab the cover form a URL.  Need to write that code and add cover images.
- Not handling Format (Hardback, Paperback, Trade Paper, Mass Market Paperback) and all of the variations to same.

## Anything Else?

I'd like at some point to handle sharing the Calibre information on the web.  There's a built-in Calibre content server, but I'd like something more robust.  We'll see.

## References 

### Calibre 

1. [calibredb documentation](https://manual.calibre-ebook.com/generated/en/calibredb.html)

### DeliciousLibrary

2. [DeliciousLibrary on Wikipedia](https://en.wikipedia.org/wiki/Delicious_Library)
3. [Message from Wil Shipley](https://mastodon.social/@wjs/113539330521476328) about what went wrong.
4. [Redit thread](https://www.reddit.com/r/macapps/comments/1gjwlci/is_delicious_library_finally_dead/) on the passing of Delicious Library. 

### Other work

5. Simualtine has some notes on [using Python to access Calibre](https://simulatine.github.io/100DaysOfCode/day-6-python-and-calibre.html)
6. Davide Aversa has a post on [using Calibre for tracking physical books](https://www.davideaversa.it/blog/how-calibre-manage-physical-library/)
