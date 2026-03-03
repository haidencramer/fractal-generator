import json
import os
from generator.fractal import generate_julia
from generator.weather import get_weather_data
from generator.audio import generate_weather_tone

def main():
    print("--- Fractal & Audio Observer Update ---")
    
    # 1. Fetch live Missoula data
    weather = get_weather_data()
    temp = weather.get("temp")
    humidity = weather.get("humidity")
    wind = weather.get("wind")
    
    # 2. Update Fractal (Static Image)
    c_const = complex(-0.7 + (temp / 100), 0.27 + (humidity / 1000))
    os.makedirs("static", exist_ok=True)
    generate_julia(c_const, "static/latest_fractal.png")
    
    # 3. Update Audio & Spectrogram
    actual_freq = generate_weather_tone(wind)
    
    # 4. Save JSON for the Website
    stats = {
        "temp": temp, "humidity": humidity, "wind": wind,
        "freq": round(actual_freq, 2),
        "c_real": round(c_const.real, 4), "c_imag": round(c_const.imag, 4)
    }
    with open("static/weather_stats.json", "w") as f:
        json.dump(stats, f)
    
    print(f"Success: Updated fractal and audio for {temp}°C and {wind}m/s wind.")

if __name__ == "__main__":
    main()