import json
import os
import pathlib
import re
from create_sets import tweaks
#! How to know when a tweak is apply or revert??????????????????????????????????????????????

# (1). Read File (open file)
# (2). Split contents (only needed info)
# (3). Split the split contents (Hive, Path, etc.) 
#* ^^^ -> Reading Data ( DONE )

# (1). Traverse folders
# (2). Find File ---------------------|
# (3). Save FileName                  \
# (4). Find Other filename for revert | ---> But when is it revert? :c
# (5). Search FilePath of the File----\
#* ^^^ -> Getting path & name ( DONE )

# (1). Write the split data into tweaks.json file
#* ^^^ -> Writing Data : ( X )

def get_tweak_name(filepath:str):
    print(filepath)

def get_file_contents(filepath:str):
    try:
        if '.reg' in filepath:
            with open(filepath, "r") as file:
                return file.read()
            
        elif '.bat' in filepath:
            with open(filepath, "r", encoding="utf-8") as file:
                return file.readlines()
    except AttributeError as e:
        raise e


def parse_tweak_contents(filepath:str, tweakContents: str | list[str] | None):
    print('filepath:::', filepath)
    if ".reg" in filepath:
        pattern = re.compile(
            r'\[(HKEY_[A-Z_]+)\\([^\]]+)\][\s\S]*?"([^"]+)"=(dword|hex|hex\(2\)|sz):?([0-9a-fA-F,"]*)',
            re.IGNORECASE
        )
        
        content = get_file_contents(filepath)
        name = 'test'
        
        tweak = {name : []}      
        regexSearch = re.search(pattern, tweakContents)

        if regexSearch:
            function = "add"
            hive = regexSearch.group(1)
            path = regexSearch.group(2)
            name = regexSearch.group(3)
            value = regexSearch.group(5)
            
            
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
        else:
            print("not found")
            
    else:
        pattern = re.compile(
            r'^reg(?:\.exe)?\s+'
            r'(add|delete)\s+'                     
            r'"(HKLM|HKCU|HKCR|HKU|HKCC|HKEY_LOCAL_MACHINE|HKEY_CURRENT_USER|HKEY_CLASSES_ROOT|HKEY_USERS|HKEY_CURRENT_CONFIG)\\([^"]+)"' 
            r'(?:\s+/v\s+"?([^"\s]+)"?)?'       
            r'(?:\s+/t\s+(REG_\w+))?'             
            r'(?:\s+/d\s+"?([^"]+)"?)?'           
            r'(?:\s+/f)?$',                       
            re.IGNORECASE
        )
        
        
        
        
        tweak = []      

        for line in tweakContents:
            
            regexSearch = re.match(pattern, line)
            
            if regexSearch:
                function = regexSearch.group(1)
                hive     = regexSearch.group(2)
                path     = regexSearch.group(3)
                name     = regexSearch.group(4)       
                # rtype    = regexSearch.group(5)       
                value    = regexSearch.group(6)       
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
        
        
    return tweak


        #? Writes the tweak
        
        # with open("tweaks.json", 'r') as f:
        #     try:
        #         data = json.load(f)
        #     except json.JSONDecodeError:
        #         data = {}
            
        # data.update(tweak)

        # with open ("tweaks.json", 'w') as f:
        #     json.dump(data, f, indent=4)


            # 
            # 'Tweak_Files\Main_Tweaks\Event_Processor_Registry\Default_Event_Processor.reg'
      
def write_tweak(parsedTweakData):
    with open("tweaks.json", 'r') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = {}
            
    data = [parsedTweakData]
    
    print("Data:", data)
    print(parsedTweakData)
    
    with open ("tweaks.json", 'w') as f:
        json.dump(data, f, indent=4)

      
tweakArray = []
      
def parse_tweaks(tweaksArray):
    for tweak in tweaksArray:  
        print(next(iter(tweak.values()))[0])
        path = next(iter(tweak.keys()))
        tweak = next(iter(tweak.values()))[0]

        applyTweak = tweak['apply']
        revertTweak = tweak['revert']
        
        # print('path;;', path)
        # print(applyTweak) # RmGpsPsEnablePerCpuCoreDpc.reg
        # print(revertTweak) # Revert_RmGpsPsEnablePerCpuCoreDpc.bat
        
        applyTweakpath = os.path.join(path, applyTweak)
        revertTweakpath = os.path.join(path, revertTweak)
        
        # print(applyTweakpath)

        applyContents = get_file_contents(applyTweakpath)
        revertContents = get_file_contents(revertTweakpath)
        
        parsedApplyTweak = parse_tweak_contents(applyTweakpath, applyContents)
        parsedRevertTweak = parse_tweak_contents(revertTweakpath, revertContents)
        
        tweakArray.append({"apply":[parsedApplyTweak], "revert": [ parsedRevertTweak]})


        # path = next(iter(tweak.keys()))
        
        # applyValue = next(iter(tweak.values()))[0]['apply']    
        # applyTweak = path + "\\" + applyValue
        # write_tweak(applyTweak, "h")
  
      
parse_tweaks(tweaks)

write_tweak(tweakArray)


# write_tweak(r"Rewrite_Tweaks\tweaks\tweakytweak\INTEL\Increase_the_number_of_kernel_threads.bat") 