import json
import os
import pathlib
import re
from create_sets import tweaks
#! How to know when a tweak is apply or revert??????????????????????????????????????????????

# (1). Read File (open file)
# (2). Split contents (only needed info)
# (3). Split the split contents (Hive, Path, etc.)
# * ^^^ -> Reading Data ( DONE )

# (1). Traverse folders
# (2). Find File ---------------------|
# (3). Save FileName                  \
# (4). Find Other filename for revert | ---> But when is it revert? :c
# (5). Search FilePath of the File----\
# * ^^^ -> Getting path & name ( DONE )

# (1). Write the split data into tweaks.json file
# * ^^^ -> Writing Data : ( X )


def get_tweak_name(filepath: str):
    print(filepath)
    match = re.search(r'[^\\]+$', filepath)
    if match:
        name = match.group(0)
        name = name.strip('Apply')
        name = name.strip('apply')
        if name[0] == "_":
            name = name[1:]
            
        if ".reg" in name:
            name = name.strip('.reg')
            print(name)
            return name
        elif ".bat" in name:
            name = name.strip('.bat')
            print(name)
            return name


def get_file_contents(filepath: str):
    try:
        if '.reg' in filepath:
            with open(filepath, "r") as file:
                return file.read()

        elif '.bat' in filepath:
            with open(filepath, "r", encoding="utf-8") as file:
                return file.readlines()
    except AttributeError as e:
        raise e


def parse_tweak_contents(filepath: str, tweakContents):
    if ".reg" in filepath:
        print('reg')
        pattern = re.compile(
            r'\[(HKEY_[A-Z_]+)\\([^\]]+)\][\s\S]*?"([^"]+)"=(dword|hex|hex\(2\)):(\w+)',
            re.IGNORECASE
        )
        name = get_tweak_name(filepath)
        tweak = {name: []}
        regexSearch = re.search(pattern, tweakContents)
        if regexSearch:
            tweak[list(tweak)[0]].append({
                "function": "add",
                "hive": regexSearch.group(1),
                "path": regexSearch.group(2),
                "name": regexSearch.group(3),
                "value": regexSearch.group(5)
            })
        else:
            print("not found")
            
    else:
        pattern = re.compile(
            r'^reg(?:\.exe)?\s+'
            r'(add|delete)\s+'
            r'"(HKLM|HKCU|HKCR|HKU|HKCC|HKEY_LOCAL_MACHINE|HKEY_CURRENT_USER|HKEY_CLASSES_ROOT|HKEY_USERS|HKEY_CURRENT_CONFIG)\\([^"]+)"'
            r'(?:\s+/v\s+"?([^"\s]+)"?)?'
            r'(?:\s+/t\s+(REG_\w+))?'
            r'(?:\s+/d\s+(?:"([^"]+)"|([^\s/]+)))?'
            r'(?:\s+/f)?\s*$',
            re.IGNORECASE
        )
        name = get_tweak_name(filepath)
        tweak = {name: []}

        for line in tweakContents:
            regexSearch = re.match(pattern, line)

            if regexSearch:
                tweak[list(tweak)[0]].append({
                    'function': regexSearch.group(1),
                    'hive': regexSearch.group(2),
                    'path': regexSearch.group(3),
                    'name': regexSearch.group(4),
                    'value': regexSearch.group(6) or regexSearch.group(7)
                })

    return tweak


def write_tweak(parsedTweakData):
    with open("tweaks.json", 'r') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            data = {}

    data = [parsedTweakData]

    # print("Data:", data)
    # print(parsedTweakData)

    with open("tweaks.json", 'w') as f:
        json.dump(data, f, indent=4)


tweakArray = []
def parse_tweaks(tweaksArray):
    for tweak in tweaksArray:
        path = next(iter(tweak.keys()))
        tweak = next(iter(tweak.values()))[0]
        applyTweak = tweak['apply']
        revertTweak = tweak['revert']

        applyTweakpath = os.path.join(path, applyTweak)
        revertTweakpath = os.path.join(path, revertTweak)

        name = get_tweak_name(applyTweakpath)


        applyContents = get_file_contents(applyTweakpath)
        revertContents = get_file_contents(revertTweakpath)

        parsedApplyTweak = parse_tweak_contents(applyTweakpath, applyContents)
        parsedRevertTweak = parse_tweak_contents(revertTweakpath, revertContents)

        print('parsed cotentsn::', parsedApplyTweak)
        
        tweakArray.append({name: {"apply":[parsedApplyTweak], "revert": [ parsedRevertTweak]}})


parse_tweaks(tweaks)
write_tweak(tweakArray)
