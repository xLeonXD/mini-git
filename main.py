import shutil as sh
import os


def commit_single(file: str,gitname: str) -> bool:
    try:
        file_name = os.path.basename(file)
        path = os.path.dirname(file)
        os.makedirs(f"mini_git/commit/{gitname}/{path}", exist_ok=True)
        sh.copy2(file,f"mini_git/commit/{gitname}/{path}/{file_name}")
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

