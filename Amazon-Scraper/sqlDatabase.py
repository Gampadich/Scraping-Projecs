import sqlite3
import asyncio

async def setupSQL():
    conn = sqlite3.connect('pages.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS pages (
        page INTEGER NOT NULL
    )
    ''')
    cursor.execute('''SELECT page FROM pages''')
    row = cursor.fetchone()

    if row is None:
        cursor.execute('''INSERT INTO pages (page) VALUES (1)''')
        conn.commit()

    conn.commit()
    cursor.close()
    conn.close()

async def setPages(pages):
    conn = sqlite3.connect('pages.db')
    cursor = conn.cursor()

    cursor.execute('''UPDATE pages SET page = ?''', (pages,))

    conn.commit()
    cursor.close()
    conn.close()

async def deletePages():
    conn = sqlite3.connect('pages.db')
    cursor = conn.cursor()

    cursor.execute('''DELETE FROM pages WHERE page''')

    conn.commit()
    cursor.close()
    conn.close()

asyncio.run(deletePages())

async def getPages():
    conn = sqlite3.connect('pages.db')
    cursor = conn.cursor()

    cursor.execute('''SELECT page FROM pages''')
    result = cursor.fetchone()

    conn.commit()
    cursor.close()
    conn.close()

    return result[0]