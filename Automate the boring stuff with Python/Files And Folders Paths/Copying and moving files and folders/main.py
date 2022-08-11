# import shutil

# shutil.copy("file path", "destination path") => copies the file to the destination path

# we can also copy and rename by specifying a new name in the destination path:

# shutil.copy("file path", "destination path/renamed.txt")

# we can copy a full folder through the use of:
# shutil.copytree("folder to copy path", "new path for the copied folder")

# we can move a file to a different location:
# shutil.move("file to move path", "new folder path")

# we can use the move() method to rename the file
# shutil.move("file to move path", "file to move path/newName.txt")