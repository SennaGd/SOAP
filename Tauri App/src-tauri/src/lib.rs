// Learn more about Tauri commands at https://tauri.app/develop/calling-rust/
use windows_registry::*;

fn registry()->Result<()> {
    let key = CURRENT_USER.create("software\\windows-rs")?;

    key.set_u32("number", 123)?;
    key.set_string("name", "Rust")?;

    println!("{}", key.get_u32("number")?);
    println!("{}", key.get_string("name")?);

    Ok(())
}

#[tauri::command]
fn greet(name: &str) -> String {

    let _ = registry();

    format!("Hello, {}! You've been greeted from Rust!", name)
}

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    tauri::Builder::default()
        .plugin(tauri_plugin_opener::init())
        .invoke_handler(tauri::generate_handler![greet])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
