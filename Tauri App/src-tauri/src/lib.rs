#![allow(unused)]
use winreg::{HKLM, HKCC, HKCU};
use winreg::enums::*;
use winreg::RegKey;

use std::path::Path;
use std::io;

#[derive(Debug)]
enum RegistryValue<'a> {
    Dword(u32),
    Sz(&'a str),
    Null(&'a str),
}

enum TweakValue<'a> {
   Str(&'a str),
   Int(u32),
}

#[tauri::command]
fn key_handler(function: &str, hive: &str, path: &str, key_name: &str, key_value: &str) -> Result<(), String> {
    let (_key, parsed_tweak) = differentiate_key_types(&key_value);
    let mut parsed_hive: &RegKey = HKLM;
    match hive {
        "HKEY_LOCAL_MACHINE"   => {parsed_hive = HKLM;},
        "HKEY_CURRENT_USER"    => {parsed_hive = HKCU;},
        "HKEY_CURRENT_CONFIG"  => {parsed_hive = HKCC;},
        &_                     => {parsed_hive = HKLM;}, // default hive: HKEY_LOCAL_MACHINE
    }

    dbg!(&hive);

    let parsed_path = Path::new(&path);
    let (key, disp) = &parsed_hive.create_subkey(&parsed_path).map_err(|e| e.to_string())?;
    match disp {
       REG_CREATED_NEW_KEY => println!("A new key created."),
       REG_OPENED_EXISTING_KEY => println!("Existing key was opened."),
    }

    // Parsing key_value to either be an i32/&str
    
    key.set_value(&key_name, &key_value).unwrap();
    Ok(())
}
//    // -- init value
//
//
//    // -- fetch type of tweak value
//    match parsed_tweak{
//        RegistryValue::Dword(num) => {
//            value = TweakValue::Int(num);
//        },
//        RegistryValue::Sz(num) => {
//            value = TweakValue::Str(num);
//        },
//        RegistryValue::Null(num) => {
//            value = TweakValue::Str(num);
//        }
//    }
//
//    match value {
//        TweakValue::Int(num) => {
//            if function == "add" {
//                println!("Creating new DWORD: {}", &key_name);
//                key.set_value(&key_name, &num).unwrap();
//            } else { 
//                key.delete_value(&key_name)?; 
//            }
//        },
//        TweakValue::Str(num) => {
//            if function == "add" {
//                key.set_value(&key_name, &num).unwrap();
//            } else { 
//                key.delete_value(&key_name)?; 
//            }
//        }
//    }
//
//    Ok(())





fn differentiate_key_types(key_value: &str) -> (&'static str, RegistryValue) {
    // first try integer parsing:
    let int_value: Result<i32, _> = key_value.parse();
    match int_value {
        Ok(number) => {
            let num = get_dword_value(&number);
           ( "REG_DWORD", RegistryValue::Dword(num))
        },
        Err(_) => {
            if key_value.to_lowercase() == "null" {
                ( "Err", RegistryValue::Null(key_value)) 
            } 
            else {
                ( "Sz", RegistryValue::Sz(key_value))
            }
        },
    }
}

fn get_dword_value(int_key_value: &i32) -> u32 {
    let length_key_val = int_key_value.to_string(); 
    let val_str = length_key_val.to_string();
    let mut total = 0;
    for i in 0..length_key_val.len() {
        let val_number: i32;

        let int_val_len = length_key_val.len();
        let hex_type: i32 = 16;
        let reversed_nums = int_val_len-i-1;
        
        let index_val = val_str.chars()
                               .nth(reversed_nums)
                               .unwrap();

        let int_val = index_val.to_string()
                               .parse();

        match int_val {
            Ok(number) => { val_number = number},
            Err(_) => { 
                println!("Given key value is not a number.");
                return 0; 
            }
        }

        let int_index: u32 = i as u32;
        let weight = hex_type.pow(int_index);
        let value = val_number * weight;

        total = total + value
    }
    println!("{}", total);
    let total_u32: u32 = total as u32;
    return total_u32;
}

#[tauri::command]
fn hello(title: &str) {
	println!("Hello {}", title);
}

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    tauri::Builder::default()
        .plugin(tauri_plugin_opener::init())

        .invoke_handler(tauri::generate_handler![key_handler])

        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
