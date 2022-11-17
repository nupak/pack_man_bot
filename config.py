import os
from dotenv import load_dotenv

load_dotenv()
path_to_files = os.getenv("PATH_TO_FILES")
TOKEN = os.getenv('TOKEN')
DEBUG = os.getenv("DEBUG")
ADMIN_ID = os.getenv("ADMIN_ID")

def isDebug(DEBUG):
    return DEBUG.upper() == "YES"