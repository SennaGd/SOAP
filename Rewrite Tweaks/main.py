import os, json, re


#! How to know when a tweak is apply or revert??????????????????????????????????????????????

# (1). Read File (open file)
# (2). Split contents (only needed info)
# (3). Split the split contents (Hive, Path, etc.) 
#* ^^^ -> Reading Data

# (1). Traverse folders
# (2). Find File -------------------|
# (3). Save FileName                |
# (4). Search FilePath of the File--|
#* ^^^ -> Getting path & name

# (1). Write the split data into tweaks.json file
#* ^^^ -> Writing Data

tweakPath = "./testfile.bat"

pattern = re.compile(
    r'^reg(?:\.exe)?\s+(add|delete)\s+"((HKLM|HKCU|HKCR|HKU|HKCC|'
    r'HKEY_LOCAL_MACHINE|HKEY_CURRENT_USER|HKEY_CLASSES_ROOT|'
    r'HKEY_USERS|HKEY_CURRENT_CONFIG)\\([^"]+))"'
    r'(?:\s+/v\s+"([^"]+)")?'
    r'(?:\s+/t\s+(REG_\w+))?'
    r'(?:\s+/d\s+"?([^"]+)"?)?'
    r'(?:\s+/f)?$',
    re.IGNORECASE
)
i = 0
with open(tweakPath, "r") as file:
    name = file.name.split('./')[-1]
    content = file.readlines()

print(name.split('./')[-1], ": Contents")
tweak = {name : []}        

for line in content:
    regexSearch = re.match(pattern, line)
    if regexSearch:
        function = regexSearch.group(1)
        hive = regexSearch.group(3)
        path = regexSearch.group(4)
        name = regexSearch.group(5)
        value = regexSearch.group(6)
        path = path.replace("\\", "\\\\")
        # print("\nfunction: ", function)
        # print("hive: ", hive)
        # print("path: ", path)
        # print("name: ", name)
        # print("value ", value)
        
        tweak[list(tweak)[0]].append({
            'function':function,
            'hive':hive,
            'path':path,
            'name':name,
            'value':value
        })
        
for x in tweak:
    for y in tweak[x]:
        print(y)
        