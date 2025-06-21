import os

# Specify the directory (you can also use '.' for the current directory)
directory_path = '.'  # Current directory

try:
    # Get the list of files and directories
    contents = os.listdir(directory_path)

    print(f"Contents of '{directory_path}':")
    for item in contents:
        print(item)

except FileNotFoundError:
    print(f"The directory '{directory_path}' was not found.")
except PermissionError:
    print(f"Permission denied to access '{directory_path}'.")
