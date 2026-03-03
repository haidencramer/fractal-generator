import json
import os
from generator.fractal import generate_julia
from generator.weather import get_weather_data  #

def main():
    print("--- Fractal Generator Observer Update ---")
    
    # 1. Fetch real-time data for Missoula
    weather = get_weather_data()
    
    # 2. Extract the real values from the API response
    temp = weather.get("temp")
    humidity = weather.get("humidity")
    wind_speed = weather.get("wind")
    
    # 3. Map real weather to fractal math
    # Temperature shifts the real part, Humidity shifts the imaginary part
    c_const = complex(-0.7 + (temp / 100), 0.27 + (humidity / 1000))
    
    print(f"LIVE Conditions: {temp}C, Humidity: {humidity}%")
    print(f"Generating Fractal with seed: {c_const}")

    # Ensure static directory exists
    os.makedirs("static", exist_ok=True)

    zoom_level = 1.0 + (wind_speed / 10)

    # 4. Generate with the new live parameters
    generate_julia(c_const, filename="static/latest_fractal.png", zoom=zoom_level)
    
    # 5. Save real stats for the Web Dashboard
    stats = {
        "temp": temp,
        "humidity": humidity,
        "wind_speed": wind_speed,
        "c_real": round(c_const.real, 4),
        "c_imag": round(c_const.imag, 4)
    }
    
    with open("static/weather_stats.json", "w") as f:
        json.dump(stats, f)
    
    print("Update Successful with Live API Data.")

if __name__ == "__main__":
    main()