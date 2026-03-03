import json
import os
from generator.fractal import generate_julia
# from generator.audio import generate_audio  # Uncomment when ready

def main():
    print("--- Fractal Generator Observer Update ---")
    
    # Mock weather data (replace with your actual weather API call)
    temp = 10.5
    humidity = 32
    wind_speed = 6.9
    
    # Map weather to fractal math
    # Temperature shifts the real part, Humidity shifts the imaginary part
    c_const = complex(-0.7 + (temp / 100), 0.27 + (humidity / 1000))
    
    print(f"Conditions: {temp}C, Humidity: {humidity}%")
    print(f"Generating Fractal with seed: {c_const}")

    # Ensure static directory exists
    os.makedirs("static", exist_ok=True)

    zoom_level = 1.0 + (wind_speed / 10)

    # Generate with the new zoom parameter
    generate_julia(c_const, filename="static/latest_fractal.png", zoom=zoom_level)
    # 2. Save Stats for the Web Dashboard
    stats = {
        "temp": temp,
        "humidity": humidity,
        "c_real": round(c_const.real, 4),
        "c_imag": round(c_const.imag, 4)
    }
    
    with open("static/weather_stats.json", "w") as f:
        json.dump(stats, f)
    
    print("Update Successful.")

if __name__ == "__main__":
    main()