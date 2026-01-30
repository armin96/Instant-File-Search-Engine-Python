import sqlite3

DB_FILE = "files.db"
LIMIT = 50

def parse_query(query):
    """
    Parses search input.
    Examples:
      'resume .pdf' -> ('resume', '.pdf')
      '.jpg'        -> (None, '.jpg')
      'report'     -> ('report', None)
    """
    name = None
    ext = None

    for part in query.lower().split():
        if part.startswith("."):
            ext = part
        else:
            name = part

    return name, ext

def search_files(name, ext):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    sql = "SELECT path FROM files WHERE 1=1"
    params = []

    if name:
        sql += " AND name LIKE ?"
        params.append(f"{name}%")

    if ext:
        sql += " AND name LIKE ?"
        params.append(f"%{ext}")

    sql += " LIMIT ?"
    params.append(LIMIT)

    cursor.execute(sql, params)
    results = cursor.fetchall()
    conn.close()

    return results

if __name__ == "__main__":
    print("Instant File Search")
    print("Search by filename, extension, or both")
    print("Examples: resume | .pdf | resume .pdf")
    print("Type 'exit' to quit\n")

    while True:
        query = input("Search: ").strip()
        if query.lower() == "exit":
            break

        name, ext = parse_query(query)
        results = search_files(name, ext)

        if not results:
            print("No results found\n")
        else:
            for r in results:
                print(r[0])
            print()
