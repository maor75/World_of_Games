import os
import platform
SCORES_FILE_NAME = "scores.txt"
BAD_RETURN_CODE = -1

def Screen_cleaner():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")