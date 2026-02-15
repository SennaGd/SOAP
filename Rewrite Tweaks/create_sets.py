import os
from find_tweak_folder import getTweakFolders


def getTweakSets(folderList: list) -> list:
    revertMap = [
        "revert", "Revert",
        "default", "Default"
    ]

    tweaks = []
    for folder in folderList:
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
                    rFile = rFile.split(revert+"_")

            if (len(rFile) == 2):
                reverFile = rFile[1]
            else:
                reverFile = rFile[0]

            if ".bat" in reverFile:
                reverFile = reverFile.strip(".bat")
            elif ".reg" in reverFile:
                reverFile = reverFile.strip(".reg")

            for aFile in applyFiles:
                if reverFile in aFile:
                    filesArray.append(
                        {"apply": aFile, "revert": revertFile[0]})

        if filesArray != []:
            tweaks.append({folder: filesArray})
        else:
            pass

    return tweaks


tweakFolders = getTweakFolders("Tweak Files")
tweaks = getTweakSets(tweakFolders)

for x in tweaks:
    print(x)
