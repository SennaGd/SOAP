import subprocess

def switch_enabled(button,true_false_switch,filetype_apply,filetype_revert,apply_filepath,undo_filepath):
    """ 
    Runs registry or batch files. It takes two filepaths to reg or bat files and two filetypes of the files.
    
    
    Args:
        true_false_switch (is always just "self"): Used to define the 'is_enabled' in a class.
        
        filetype_apply (String): can be either set to 'reg','bat'
        
        filetype_revert (String): can be either set to 'reg','bat'
        
        apply_filepath (String): Tweaks\\filepath
        
        undo_filepath (String): Tweaks\\filepath
    """
    true_false_switch.EnableDisable = "Apply" if true_false_switch.is_enabled else "Revert"
    button.configure(text=true_false_switch.EnableDisable)
    true_false_switch.is_enabled = not true_false_switch.is_enabled
    
    print(f"is_enabled = {true_false_switch.is_enabled}")
    if true_false_switch.is_enabled:
        if filetype_apply == 'bat':
            subprocess.run(["cmd.exe",'/c',f"Tweaks\\{apply_filepath}.{filetype_apply}"],shell=True)
            print(f"Tweaks\\{apply_filepath}.{filetype_apply}")
        elif filetype_apply == 'reg':
            subprocess.run(['reg','import',f"Tweaks\\{apply_filepath}.{filetype_apply}"],shell=True)
    else:
        if filetype_revert == 'bat':
            subprocess.run(["cmd.exe",'/c',f"Tweaks\\{undo_filepath}.{filetype_revert}"],shell=True)
        elif filetype_revert == 'reg':
            subprocess.run(['reg','import',f"Tweaks\\{undo_filepath}.{filetype_revert}"],shell=True)