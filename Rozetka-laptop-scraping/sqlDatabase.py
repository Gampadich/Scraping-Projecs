import sqlite3


async def setupSQL():
    # Connect to the SQLite database file
    conn = sqlite3.connect('pages.db')
    cursor = conn.cursor()

    # Create the 'pages' table if it doesn't already exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS pages (
        page INTEGER NOT NULL
    )
    ''')

    # Check if a page record already exists
    cursor.execute('''SELECT page FROM pages''')
    row = cursor.fetchone()

    # Insert initial page state (1) if table is empty
    if row is None:
        cursor.execute('''INSERT INTO pages (page) VALUES (1)''')
        conn.commit()

    # Finalize transaction and close connection resources
    conn.commit()
    cursor.close()
    conn.close()


async def setPages(pages):
    # Connect to the database
    conn = sqlite3.connect('pages.db')
    cursor = conn.cursor()

    # Update the stored page number with the new value
    cursor.execute('''UPDATE pages SET page = ?''', (pages,))

    # Save changes and clean up connection
    conn.commit()
    cursor.close()
    conn.close()


async def deletePages():
    # Connect to the database
    conn = sqlite3.connect('pages.db')
    cursor = conn.cursor()

    # Delete records from the pages table
    cursor.execute('''DELETE FROM pages WHERE page''')

    # Save changes and clean up connection
    conn.commit()
    cursor.close()
    conn.close()


async def getPages():
    # Connect to the database
    conn = sqlite3.connect('pages.db')
    cursor = conn.cursor()

    # Fetch the stored page number
    cursor.execute('''SELECT page FROM pages''')
    result = cursor.fetchone()

    # Clean up connection
    conn.commit()
    cursor.close()
    conn.close()

    # Return the fetched page value
    return result[0]