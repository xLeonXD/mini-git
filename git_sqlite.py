import sqlite3 as sql

def create_table_commit() -> None:
    with sql.connect("git.db") as con:
        cursor = con.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS commits("
                       "id INTEGER PRIMARY KEY,"
                       "message TEXT DEFAULT 'none',"
                       "timestamp TEXT DEFAULT CURRENT_TIMESTAMP"
                       ")")

def insert_git_data(message: str = "") -> None:
    with sql.connect("git.db") as con:
        cursor = con.cursor()
        cursor.execute("INSERT INTO commits (message) VALUES (?)",[message])
        try:
            con.commit()
        except Exception as err:
            print(f"ERROR : {err}")
            print("Rolling back!")
            con.rollback()
            
