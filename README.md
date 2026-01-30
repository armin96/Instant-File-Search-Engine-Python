# Instant File Search Engine Python

A fast file search tool.
This project indexes file names once and provides instant search by filename and file extension.

==================================================

FEATURES
--------

- One-time file indexing
- Instant search (no disk scanning during search)
- Search by:
  - File name
  - File extension (.pdf, .jpg, etc.)
  - File name + extension combined
- SQLite database optimized for speed
- Cross-platform (Windows, Linux, macOS)
- No external dependencies

==================================================

HOW IT WORKS
------------

1. The file system is scanned once
2. File names and full paths are stored in an SQLite database
3. Searches are performed against the database, not the disk
4. Results are returned instantly

NOTE:
File contents are NOT indexed 

==================================================


IMPORTANT:
The files.db file should NOT be uploaded to GitHub.
It is generated automatically after indexing.

==================================================

USAGE
-----

STEP 1: INDEX FILES (RUN ONCE)

Run:
python indexer.py

When prompted, enter a path to index, for example:
C:/Users/YourName

Output example:
Indexing completed — 120000 files indexed

--------------------------------------------------

STEP 2: SEARCH INSTANTLY

Run:
python search.py

Example searches:
resume
.pdf
resume .pdf
photo .jpg
report .docx

Type 'exit' to quit.

==================================================

PERFORMANCE
-----------

- Uses bulk inserts for fast indexing
- SQLite optimized with performance pragmas
- Indexed queries for instant search
- Handles tens or hundreds of thousands of files efficiently

