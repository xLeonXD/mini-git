import shutil as sh
import os
import git_sqlite as sql

"""
TODO LIST :

add sqlite for list of commits DONE

change commit in a way that it makes a copy of each commit to save the old version DONE

get uploaded version

add username to commits

add accounts

"""

def commit_single(file: str,gitname: str,message: str = "") -> bool:
    try:
        git_id = sql.insert_git_data(message, gitname,1)
        if git_id is None:
           git_id = 1
        file_name = os.path.basename(file)
        path = os.path.dirname(file)
        os.makedirs(f"mini_git/commit/{gitname}/{git_id}/{path}", exist_ok=True)
        sh.copy2(file,f"mini_git/commit/{gitname}/{git_id}/{path}/{file_name}")
        print("File copied successfully")
        return True
    except FileNotFoundError:
        print("Source file not found")
        return False
    except PermissionError:
        print("Permission denied")
        return False
    except Exception as error:
        print(f"Error : {error}")
        return False

def commit_whole(folder : str) -> bool:
    try:
        folder_name = os.path.basename(folder)
        path = os.path.dirname(folder)
        os.makedirs(f"mini_git/commit/{path}",exist_ok=True)
        sh.copytree(folder,f"mini_git/commit/{path}/{folder_name}")
        return True
    except FileNotFoundError:
        print("Source file not found")
        return False
    except PermissionError:
        print("Permission denied")
        return False
    except Exception as error:
        print(f"Error : {error}")
        return False

def see_commit_history():
    items = sql.show_commits_history()
    if items is None:
        print("No commits history found.")
        return
    for i in items:
        print(i)
    return

def load_commit():
    pass

#commit_single("mini_git/commit/banana/abc.txt","banana")
#commit_whole("abc")
sql.create_table_commit()

#commit_single("git_sqlite.py","b","initial commit")

see_commit_history()
