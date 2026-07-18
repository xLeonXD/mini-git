import sqlite3 as sql

def create_table_commit() -> None:
    with sql.connect("git.db") as con:
        cursor = con.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS commits("
                       "id INTEGER PRIMARY KEY,"
                       "message TEXT DEFAULT 'none',"
                       "git_name TEXT NOT NULL,"
                       "git_commit_type TEXT NOT NULL "
                       "timestamp TEXT DEFAULT CURRENT_TIMESTAMP"
                       ")")

def insert_git_data(message: str,git_name: str,commit_type: int,get_id: bool = True) -> int | None:
    with sql.connect("git.db") as con:
        cursor = con.cursor()
        try:
            if commit_type == 1:
                commit_type = "Single Commit"
            elif commit_type == 2:
                commit_type = "Full Commit"
            else:
                raise "Wrong commit_type number inserted"
            cursor.execute("INSERT INTO commits (message,git_name,git_commit_type) VALUES (?,?,?)", [message, git_name,commit_type])
            if not get_id:
                return None
            #cursor.execute("SELECT id FROM commits ORDER BY id DESC")
            #return cursor.fetchone()[0]
            return cursor.lastrowid
        except Exception as err:
            print(f"ERROR : {err}")
            print("Rolling back!")

def show_commits_history(amount: int = 10):
    with sql.connect("git.db") as con:
        cursor = con.cursor()
        cursor.execute("SELECT * FROM commits ORDER BY id DESC")
        items = cursor.fetchmany(amount)
    return items
