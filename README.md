# Delicious to Calibre

## What?

The intent of this project is to convert a database (or export) of Delicious Library<sup>**2**</sup> books to a format acceptable by Calibre, and to add them to a Calibre library.  There are several ways to do this, and I'll be starting with (what I think of) as one of the simplest.

## Why?

Delicious Library was a wonderful app on macOS which tracked your physical books, and included support for both entering book data _via_ an iOS scanning app and looking up book information automatically on Amazon.

Sadly it is no more<sup>**3**</sup><sup>**4**</sup>.  A change in Amazon's fee structure for querying book data made it impractical for the authors to continue without a aubscription-based app, and so they let the project drop.

Now I have many thousands of book entries in a no longer supported app.  So...

## How?

Well, this _should_ be relatively straightforward, but... it's exploratory at this point, so I need to start by finding out more about the file formats on both sides.  

I'm going to use this a bit like a journal at first.

1. Look at the files exported by Library, and importing them into Python.  This is easy to do using CSV export from Library and import into Python.  We end up with a very large array of dictionaries.

2. Test the **calibredb** command line app<sup>**1**</sup> for various situations with a new, empty, Calibre library

3. Map the information organization in Library to the information organization in Calibre for information common to both.  For example, Calibre says "authors", Library says "creator".

4. Create meta-data for new media types.  First check to see if it's re-inventing the wheel.  There is some information available on parts of the problem<sup>**5**</sup><sup>**6**</sup>. Library supports physical books in multiple types of covers, DVDs, CDs and VHS.


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
