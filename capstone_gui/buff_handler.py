import os

def checkbuff():
    maxfilecount = 10
    # Path to the folder
    folder_path = "counted"

    # Get the list of files and directories in the folder
    files_and_dirs = os.listdir(folder_path)

    # Count only files (ignoring directories)
    file_count = sum(1 for item in files_and_dirs if os.path.isfile(os.path.join(folder_path, item)))

    print(f"There are {file_count} files in the folder.")
    
    if file_count > maxfilecount:
        # Get the list of files in the folder
        files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

        # If there are files in the folder
        if files:
            # Find the oldest file based on modification time
            oldest_file = min(files, key=os.path.getmtime)

            # Delete the oldest file
            os.remove(oldest_file)
            print(f"Deleted the oldest file: {oldest_file}")
        else:
            print("No files found in the folder.")
    else:
        print(f"File count is within the limit of {maxfilecount}.")

# Call the function
checkbuff()
