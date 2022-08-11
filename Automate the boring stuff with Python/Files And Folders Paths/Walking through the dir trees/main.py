import os

for folderName, subFolders, filenames in os.walk("./"):
    print(f"The folder is: {folderName}")
    print(f"The subfolders are: {subFolders}")
    print(f"The files are: {filenames}")