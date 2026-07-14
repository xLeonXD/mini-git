import sqlite3 as sql

def create_table_commit() -> None:
    with sql.connect("git.db") as con:
        cursor = con.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS commits("
                       "id INTEGER PRIMARY KEY,"
                       "message TEXT DEFAULT 'none',"
                       "git_name TEXT NOT NULL,"
                       "timestamp TEXT DEFAULT CURRENT_TIMESTAMP"
                       ")")

def insert_git_data(message: str,git_name: str,get_id: bool = True) -> int | None:
    with sql.connect("git.db") as con:
        cursor = con.cursor()
        try:
            cursor.execute("INSERT INTO commits (message,git_name) VALUES (?,?)", [message, git_name])
            if not get_id:
                return None
            #cursor.execute("SELECT id FROM commits ORDER BY id DESC")
            #return cursor.fetchone()[0]
            return cursor.lastrowid
        except Exception as err:
            print(f"ERROR : {err}")
            print("Rolling back!")
