import os

folder = r"C:\Users\senna\Documents\Soap\Tweak Files\Improve_system_performance_underload"

revertMap = [
    "revert", "Revert",
    "default", "Default"
]


applyFiles = []
revertFiles = []
filesArray = []

for root, dirs, files in os.walk(folder):
    for file in files:
        filesArray.append(file)


index = 0
for file in filesArray:
    for revert in revertMap:
        if revert in file:
            file = file.split()
            revertFiles.append(file)

    index += 1


index = 0
for revertFile in revertFiles:
    index = 0
    for applyFile in filesArray:
        if revertFile[0] in applyFile:
            filesArray.pop(index)

        index += 1

applyFiles = filesArray


filesArray = []
for revertFile in revertFiles:
    rFile = revertFile[0]

    for revert in revertMap:
        if revert in rFile:
            rFile = rFile.split(revert+"_")[1]

    if ".bat" in rFile:
        rFile = rFile.strip(".bat")
    elif ".reg" in rFile:
        rFile = rFile.strip(".reg")

    for aFile in applyFiles:
        if rFile in aFile:
            filesArray.append({"apply": aFile, "revert": revertFile[0]})

print(filesArray)
