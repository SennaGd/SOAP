import os


def getTweakFolders(mainFolder:str)->list:
    index = 0
    directories = []

    walkedPath = os.walk(mainFolder)

    FileFolder = []

    for root, dirs, files in walkedPath:
        directories.append([root, dirs])
        
    _ = []
    for folder in directories:
        if folder[1]:
            for y in folder[1]:
                _.append(folder[0]+'\\'+y)
                
    directories = _

    for _  in directories:
        previousIndex = index - 1
        
        if dirs == []:
            FileFolder.append(directories[previousIndex])
        
        index += 1


    index = 0
    for folder in FileFolder:
        for root, dirs, files in os.walk(folder):
            
            if files == []:
                FileFolder.pop(index)
                            
        index+=1
        
        
    return FileFolder
        