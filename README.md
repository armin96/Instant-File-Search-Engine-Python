# Instant-File-Search-Engine-Python-


# Everything-like File Search (Python)

A fast file search tool inspired by **Everything**.  
This project indexes file names once and provides **instant search** by filename and file extension.

---

## Features

- One-time file indexing
- Instant search (no disk scanning during search)
- Search by:
  - File name
  - File extension (`.pdf`, `.jpg`, etc.)
  - File name + extension combined
- SQLite database optimized for speed
- Cross-platform (Windows, Linux, macOS)
- No external dependencies

---

## How It Works

1. The file system is scanned **once**
2. File names and full paths are stored in an SQLite database
3. Searches are performed against the database, not the disk
4. Results are returned instantly

>  File contents are **not** indexed


├── indexer.py   # Builds the file index
├── search.py    # Instant search tool
├── files.db     # SQLite database (generated locally)
└── README.md


