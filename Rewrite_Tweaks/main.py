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


def parse_tweak_contents(filepath: str, tweakcontents):
    if ".reg" in filepath:
        print('reg')
        pattern = re.compile(
            r'\[(hkey_[a-z_]+)\\([^\]]+)\][\s\s]*?"([^"]+)"=(dword|hex|hex\(2\)):(\w+)',
            re.ignorecase
        )
        name = get_tweak_name(filepath)
        tweak = {name: []}
        regexsearch = re.search(pattern, tweakcontents)
        if regexsearch:
            tweak[list(tweak)[0]].append({
                "function": "add",
                "hive": regexsearch.group(1),
                "path": regexsearch.group(2),
                "name": regexsearch.group(3),
                "value": regexsearch.group(5)
            })
        else:
            print("not found")
            
    else:
        pattern = re.compile(
            r'^reg(?:\.exe)?\s+'
            r'(add|delete)\s+'
            r'"(hklm|hkcu|hkcr|hku|hkcc|hkey_local_machine|hkey_current_user|hkey_classes_root|hkey_users|hkey_current_config)\\([^"]+)"'
            r'(?:\s+/v\s+"?([^"\s]+)"?)?'
            r'(?:\s+/t\s+(reg_\w+))?'
            r'(?:\s+/d\s+(?:"([^"]+)"|([^\s/]+)))?'
            r'(?:\s+/f)?\s*$',
            re.ignorecase
        )
        name = get_tweak_name(filepath)
        tweak = {name: []}

        for line in tweakcontents:
            regexsearch = re.match(pattern, line)

            if regexsearch:
                tweak[list(tweak)[0]].append({
                    'function': regexsearch.group(1),
                    'hive': regexsearch.group(2),
                    'path': regexsearch.group(3),
                    'name': regexsearch.group(4),
                    'value': regexsearch.group(6) or regexsearch.group(7)
                })

    return tweak


def write_tweak(parsedtweakdata):
    with open("tweaks.json", 'r') as f:
        try:
            data = json.load(f)
        except json.jsondecodeerror:
            data = {}

    data = [parsedtweakdata]

    # print("data:", data)
    # print(parsedtweakdata)

    with open("tweaks.json", 'w') as f:
        json.dump(data, f, indent=4)


tweakarray = []
def parse_tweaks(tweaksarray):
    for tweak in tweaksarray:
        path = next(iter(tweak.keys()))
        tweak = next(iter(tweak.values()))[0]
        applytweak = tweak['apply']
        reverttweak = tweak['revert']

        applytweakpath = os.path.join(path, applytweak)
        reverttweakpath = os.path.join(path, reverttweak)

        name = get_tweak_name(applytweakpath)


        applycontents = get_file_contents(applytweakpath)
        revertcontents = get_file_contents(reverttweakpath)

        parsedapplytweak = parse_tweak_contents(applytweakpath, applycontents)
        parsedreverttweak = parse_tweak_contents(reverttweakpath, revertcontents)

        print('parsed cotentsn::', parsedapplytweak)
        
        tweakarray.append({name: {"apply":[parsedapplytweak], "revert": [ parsedreverttweak]}})


parse_tweaks(tweaks)
write_tweak(tweakArray)
