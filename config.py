import os
from dotenv import load_dotenv

load_dotenv()
path_to_files = os.getenv("PATH_TO_FILES")
TOKEN = os.getenv('TOKEN')
DEBUG = os.getenv("DEBUG")
ADMIN_ID = os.getenv("ADMIN_ID")
VIP_LIST = [303401713, 300362746]
def isDebug(DEBUG):
    return DEBUG.upper() == "YES"