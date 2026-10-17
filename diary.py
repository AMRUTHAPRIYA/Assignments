# Task 3: Diary Entry Program (File I/O and OS Operations)
# This script uses the 'os' module to check files and 'datetime' to add timestamps.

import os
import datetime

def manage_diary():
    filename = "diary.txt"
    
    try:
        # Check if diary.txt already exists in the folder
        if not os.path.exists(filename):
            print(f"'{filename}' not found. Creating a new diary file for you...")
            # Open in write mode ("w") just to create an empty file
            with open(filename, "w") as f:
                pass 

        # Ask the user to type their entry
        entry = input("Enter your diary entry: ")
        
        # Get the current date and time and format it nicely
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Open in append mode ("a") so we add to the file without erasing past entries
        with open(filename, "a") as f:
            f.write(f"[{timestamp}] {entry}\n")
            
        print("\n--- Past and Current Diary Entries ---")
        
        # Open in read mode ("r") to show everything inside the diary file
        with open(filename, "r") as f:
            content = f.read()
            print(content)
            
    except IOError as e:
        print(f"An error occurred while handling the file: {e}")
    except Exception as e:
        print(f"An unexpected error happened: {e}")

if __name__ == "__main__":
    manage_diary()