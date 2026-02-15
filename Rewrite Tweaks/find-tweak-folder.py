import os

index = 0
directories = []
dirPaths = []

walkedPath = os.walk("Tweak Files")

FileFolder = []

for root, dirs, files in walkedPath:
    directories.append([root, dirs])
    
_ = []
for x in directories:
    if x[1]:
        for y in x[1]:
            _.append(x[0]+'\\'+y)
              
directories = _

for directory  in directories:
    previousIndex = index - 1
    
    if dirs == []:
        FileFolder.append(directories[previousIndex])
    
    index += 1


index = 0
for x in FileFolder:
    for root, dirs, files in os.walk(x):
        
        if files == []:
            FileFolder.pop(index)
                        
    index+=1
    
for x in FileFolder:
    print(x)
        