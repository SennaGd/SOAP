// Learn more about Tauri commands at https://tauri.app/develop/calling-rust/
//use std::io;
//use std::path::Path;
// use winreg::{RegKey, enums::*, HKEY};


/*
fn get_winreg_hive(tweak_hive: &str) -> HKEY {
    match tweak_hive {
         "HKLM" | "HKEY_LOCAL_MACHINE" => HKEY_LOCAL_MACHINE,
         "HKCU" | "HKEY_CURRENT_USER" => HKEY_CURRENT_USER,
         "HKCR" | "HKEY_CLASSES_ROOT" => HKEY_CLASSES_ROOT,   
         _ => panic!("Hive not found!")      
    }
}

fn create_key_path(tweak_hive: &str, key_path: &str) -> Result<(RegKey, RegDisposition), std::io::Error> {
    let hive = get_winreg_hive(tweak_hive);
    let hive_path = RegKey::predef(hive); // Open the hive

    let path = Path::new(key_path); // Create path instance
    let (key, disp) = hive_path.create_subkey(&path)?;// Create the path

    Ok((key, disp))
}

fn create_value<T: winreg::types::ToRegValue>(_tweak_hive: &str, _key_path: &str, data_name: &str, data_value: T) -> io::Result<()> {
    let (key, _disposition) = create_key_path(_tweak_hive, _key_path)?;
    let _ = key.set_value(data_name, &data_value);

    Ok(())
}

fn delete_value(_tweak_hive: &str, _key_path: &str, data_name: &str) -> io::Result<()> {
    let (key, _disposition) = create_key_path(_tweak_hive, _key_path)?;
    let _ = key.delete_value(&data_name)?;
    
    Ok (())
}

#[tauri::command]
fn applys() -> String {
    let i = 1u32;
                         // HIVE                 PATH                                 NAME            VALUE
    let _ = create_value("HKEY_LOCAL_MACHINE","SYSTEM\\RegTest\\TestCreatingValue", "testdata_var", i);

    format!("Hello! You've been greeted from Rust!")
}

#[tauri::command]
fn manage_registry(hive: &str, path: &str, name: &str value: T, regfunction: bool) -> String {
    let i = 1u32;
                         // HIVE                 PATH                                 NAME            VALUE
    let _ = delete_value("HKEY_LOCAL_MACHINE","SYSTEM\\RegTest\\TestCreatingValue", "testdata_var");

    format!("Hello! You've been greeted from Rust!")
}
*/

#[tauri::command]
fn hello(title: &str) {
	println!("Hello {}", title);
}

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    tauri::Builder::default()
        .plugin(tauri_plugin_opener::init())

		.invoke_handler(tauri::generate_handler![hello])
//        .invoke_handler(tauri::generate_handler![manage_registry])

        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
