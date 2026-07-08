import shutil as sh
import os


def commit_single(file: str) -> bool:
    try:
        os.makedirs("mini_git/commit", exist_ok=True)
        sh.copy2(file,f"commit/{file}")
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

