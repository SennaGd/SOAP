#![allow(unused)]

use winreg::{HKLM, HKCC, HKCU};
use winreg::enums::*;
use winreg::RegKey;

use std::ptr::null;
use std::str::FromStr;
use std::path::Path;
use std::io;

#[derive(Debug)]
enum RegistryValue {
    Dword(u32),
    Sz(String),
    Null(String),
}

enum TweakValue {
    Str(String),
    Int(u32),
}
struct Tweak<'a> {
    function: String,
    hive: &'a str,
    path: String,
    key_name: String,
    key_value: String

}
fn main() {
    let test_tweak = Tweak{
        function: String::from("add"),
        hive: "HKEY_LOCAL_MACHINE",
        path: String::from("SYSTEM\\CurrentControlSet\\services\\mouclass\\Parameters"),
        key_name: String::from("MouseSZ"),
        key_value: String::from("a")
    };

    
    key_handler(&test_tweak);
}


fn key_handler(tweak: &Tweak) -> io::Result<()> {
    let (_key1, parsed_tweak) = differentiate_key_types(&tweak.key_value);
    
    let hive = parse_hive(&tweak.hive);
    let path = Path::new(&tweak.path);

    // constructs the path or opens the path
    let (key, disp) = hive.create_subkey(&path)?;
    match disp {
       REG_CREATED_NEW_KEY => println!("A new key created."),
       REG_OPENED_EXISTING_KEY => println!("Existing key was opened."),
    }
     

    // creating or changing key values 
    // -- init value
    let mut value: TweakValue;
    value = TweakValue::Str("_".to_string());
    value = TweakValue::Int(0);

    // -- fetch type of tweak value
    match parsed_tweak{
        RegistryValue::Dword(num) => {
            value = TweakValue::Int(num);
        },
        RegistryValue::Sz(num) => {
            value = TweakValue::Str(num.clone());
        },
        RegistryValue::Null(num) => {
            value = TweakValue::Str(num.clone());
        }
    }

    match value {
        TweakValue::Int(num) => {
            if &tweak.function == "add" {
                println!("Creating new DWORD: {}", &tweak.key_name);
                key.set_value(&tweak.key_name, &num).unwrap();
            } else { 
                key.delete_value(&tweak.key_name)?; 
            }
        },
        TweakValue::Str(num) => {
            if &tweak.function == "add" {
                println!("Creating new REG_SZ: {}", &tweak.key_name);
                key.set_value(&tweak.key_name, &num).unwrap();
            } else { 
                key.delete_value(&tweak.key_name)?; 
            }
        }
    }

    Ok(())

}


fn differentiate_key_types(key_value: &String) -> (&'static str, RegistryValue) {
    // first try integer parsing:
    let int_value: Result<i32, _> = key_value.parse();
    match int_value {
        Ok(number) => {
            let num = get_dword_value(&number);
           ( "REG_DWORD", RegistryValue::Dword(num))
        },
        Err(_) => {
            if (key_value.to_lowercase() == "null") {
                ( "Err", RegistryValue::Null(key_value.clone())) 
            } 
            else {
                ( "Sz", RegistryValue::Sz(key_value.clone()))
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

fn parse_hive<'a>(hive: &'a str) -> &'a RegKey {
    match hive {
        "HKEY_LOCAL_MACHINE"=>return HKLM,
        "HKEY_CURRENT_USER"=> return HKCU,
        "HKEY_CURRENT_CONFIG"=> return HKCC,
        &_ => todo!(),
    }
}

fn create_subkey_folder(hive: &String, path: &String) {

}
