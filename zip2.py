import os
import zipfile

# Define the directory and the zip file path again
project_dir = "rust_weather_app"
zip_file_path = f"{project_dir}.zip"

# Create a new directory for the Rust project
os.makedirs(project_dir, exist_ok=True)

# Create the Cargo.toml file
cargo_toml_content = """[package]
name = "rust_weather_app"
version = "0.1.0"
edition = "2021"

[dependencies]
reqwest = { version = "0.11", features = ["json"] }
tokio = { version = "1", features = ["full"] }
serde = { version = "1.0", features = ["derive"] }
serde_json = "1.0"
"""

# Create the main.rs file
main_rs_content = """use reqwest::Error;
use serde::Deserialize;
use std::env;

#[derive(Deserialize)]
struct WeatherResponse {
    main: Main,
    weather: Vec<Weather>,
}

#[derive(Deserialize)]
struct Main {
    temp: f32,
    humidity: u32,
}

#[derive(Deserialize)]
struct Weather {
    description: String,
}

#[tokio::main]
async fn main() -> Result<(), Error> {
    let api_key = "YOUR_API_KEY"; // Replace with your OpenWeatherMap API key
    let city = env::args().nth(1).expect("Please provide a city name");

    let url = format!(
        "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric",
        city, api_key
    );

    let response: WeatherResponse = reqwest::get(&url).await?.json().await?;

    println!("Current weather in {}:", city);
    println!("Temperature: {}°C", response.main.temp);
    println!("Humidity: {}%", response.main.humidity);
    println!("Condition: {}", response.weather[0].description);

    Ok(())
}
"""

# Write the Cargo.toml file
with open(os.path.join(project_dir, "Cargo.toml"), "w") as f:
    f.write(cargo_toml_content)

# Write the main.rs file
os.makedirs(os.path.join(project_dir, "src"), exist_ok=True)
with open(os.path.join(project_dir, "src", "main.rs"), "w") as f:
    f.write(main_rs_content)

# Create a zip file of the project directory
with zipfile.ZipFile(zip_file_path, 'w') as zipf:
    for root, dirs, files in os.walk(project_dir):
        for file in files:
            zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), os.path.join(project_dir, '..')))

zip_file_path
