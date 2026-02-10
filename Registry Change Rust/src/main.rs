use std::io;
use std::path::Path;
use winreg::{RegKey};
use winreg::enums::*;
use winreg::HKEY;
use winreg::types::ToRegValue;

struct KeyValueType {
    first: &str,
    second: u32,

}

fn get_winreg_hive(tweak_hive: &str) -> HKEY {
    match tweak_hive {
         "HKLM" | "HKEY_LOCAL_MACHINE" => HKEY_LOCAL_MACHINE,
         "HKCU" | "HKEY_CURRENT_USER" => HKEY_CURRENT_USER,
         "HKCR" | "HKEY_CLASSES_ROOT" => HKEY_CLASSES_ROOT,   
         _ => panic!("Hive not found!")      
    }
}


/***
 * tweak_hive: "HKEY_LOCAL_MACHINE"
 * key_path: "SYSTEM\\CurrentControlSet\\Services\\mouclass\\Parameters"
 * value_name: "MouseDataQueueSize"
 * value_data: 25
*/
fn create_key_path(tweak_hive: &str, key_path: &str) -> Result<(RegKey, RegDisposition), std::io::Error>  {
    let hive = get_winreg_hive(tweak_hive);
    let hive_path = RegKey::predef(hive); // Open the hive
    
    let path = Path::new(key_path); // Create path instance
    let (key, disp) = hive_path.create_subkey(&path)?;// Create the path
    
    Ok((key, disp))
    }

fn create_value<T: winreg::types::ToRegValue>(_tweak_hive: &str, _key_path: &str, data_name: &str, data_value: T,u32) -> io::Result<()> {
    let (key, disposition) = create_key_path(_tweak_hive, _key_path)?;
    
    let _ = key.set_value(data_name, &val);
    // if key  {
    //     key.set_value("DWORDValue", &123u32);
        
    // }
    Ok(())
}



fn main() {
    let _ = create_value("HKEY_LOCAL_MACHINE","SYSTEM\\RegTest\\TestCreatingValue", "testdata_var", "2");


}