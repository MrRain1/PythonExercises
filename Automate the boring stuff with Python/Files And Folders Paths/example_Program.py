import os

totalSize = 0

for pathname in os.listdir("../"):
    for filename in os.listdir(os.path.join("../", pathname)):
        if not os.path.isfile(os.path.join("../"+ pathname, filename)):
            continue
        totalSize += os.path.getsize(os.path.join("../"+ pathname, filename))
        
print(totalSize)