# Deleting files

We can delete files in three ways:

1. We can use a method in the os library:

    `import os`

    `os.unlink("bacon.txt")` => **PERMANENTLY** removes a file

    `os.rmdir("folder to remove path")` => **PERMANENTLY** remove a directory only if it's an empty folder

2. We can **PERMANENTLY** remove a folder and all of its contents with the shutil module:

    `import shutil`

    `shutil.rmtree("folder to remove path")`

3. We can use the module "send2trash" to send the file to the recycle bin folder:

    `import send2trash`

    `send2trash.send2trash("folder or file path to delete")`
