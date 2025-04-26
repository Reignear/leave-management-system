import os
import mysql.connector
def get_asset(filename):
    """Returns the absolute path to an asset (image, icon, etc.)."""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    assets_dir = os.path.join(base_dir, "assets")
    return os.path.join(assets_dir, filename)
def get_db_connection():
    """Returns a new database connection."""
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # put your MySQL password here if you set one
        database="final_leave_management_db"
    )
print("utils.py loaded successfully")
