import sqlite3 as sql

def create_table_commit():
    with sql.connect("git.db") as con:
        cursor = con.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS commits("
                       "id INTEGER PRIMARY KEY,"
                       "message TEXT DEFAULT 'none',"
                       "timestamp TEXT DEFAULT CURRENT_TIMESTAMP"
                       ")")
