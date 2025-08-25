import os                   # For interacting with the operating system, like creating file paths.
import shutil               # For high-level file operations, like copying entire folder trees.
import datetime             # To work with dates, used here to get the current date for the folder name.
import schedule             # A simple library for scheduling Python jobs at specific times.
import time                 # To pause the script's execution.

source_dir = "C:/"        # The folder you want to back up.
destination_dir = "D:/"   # The location where the backup will be stored.

def copy_folder_to_directory(source, dest):
    today = datetime.date.today()   # Get today's date in YYYY-MM-DD format.
    dest_dir = os.path.join(dest, str(today))  # Create the full path for the new backup folder, e.g., "D:/2025-08-25".

    try:
        shutil.copytree(source, dest_dir)  # Recursively copy the entire source directory
        print(f"Folder copied to: {dest_dir}")
    except FileExistsError:
        print(f"Folder already exists in: {dest}")

# Backup everyday
schedule.every().day.at("6:55").do(lambda: copy_folder_to_directory(source_dir, destination_dir))

while True:
    schedule.run_pending()
    time.sleep(60)