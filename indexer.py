import os
import sqlite3

DB_FILE = "files.db"
BATCH_SIZE = 5000

def create_database(conn):
    cursor = conn.cursor()

    # SQLite performance optimizations
    cursor.execute("PRAGMA journal_mode = OFF")
    cursor.execute("PRAGMA synchronous = OFF")
    cursor.execute("PRAGMA temp_store = MEMORY")

    cursor.execute("DROP TABLE IF EXISTS files")
    cursor.execute("""
        CREATE TABLE files (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            path TEXT
        )
    """)
    cursor.execute("CREATE INDEX idx_name ON files(name)")
    conn.commit()

def index_files(base_path):
    conn = sqlite3.connect(DB_FILE)
    create_database(conn)
    cursor = conn.cursor()

    batch = []
    total_files = 0

    print("⏳ Indexing started...")

    for root, _, files in os.walk(base_path):
        for file in files:
            full_path = os.path.join(root, file)
            batch.append((file.lower(), full_path))
            total_files += 1

            if len(batch) >= BATCH_SIZE:
                cursor.executemany(
                    "INSERT INTO files (name, path) VALUES (?, ?)",
                    batch
                )
                batch.clear()

    if batch:
        cursor.executemany(
            "INSERT INTO files (name, path) VALUES (?, ?)",
            batch
        )

    conn.commit()
    conn.close()

    print(f"Indexing completed — {total_files} files indexed")

if __name__ == "__main__":
    base_path = input("Path to index (e.g. C:/Users/Armin): ").strip()
    index_files(base_path)
