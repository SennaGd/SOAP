import re


def get_file_contents(filepath:str):
    if '.reg' in filepath:
        with open(filepath, "r") as file:
            return file.read()
            
            
path = r"Tweak_Files\Main_Tweaks\Event_Processor_Registry\Disable_Event_Processor.reg"
contents = get_file_contents(path)

pattern = re.compile(
    r'\[(HKEY_[A-Z_]+)\\([^\]]+)\][\s\S]*?"([^"]+)"=(dword|hex|hex\(2\)):(\w+)',
    re.IGNORECASE
)

m = re.search(pattern, contents)

print(m.groups() if m else "NO MATCH")
