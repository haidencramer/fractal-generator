import json
import os
from generator.fractal import generate_julia
from generator.weather import get_weather_data
from generator.audio import generate_weather_tone
from datetime import datetime

def main():
    print("--- Fractal & Audio Observer Update ---")
    
    last_update = datetime.now().strftime("%b %d, %I:%M %p")
    
    weather = get_weather_data()
    temp = weather.get("temp")
    humidity = weather.get("humidity")
    wind = weather.get("wind")
    
    c_const = complex(-0.7 + (temp / 100), 0.27 + (humidity / 1000))
    os.makedirs("static", exist_ok=True)
    
    # --- FIXED LINE BELOW: We name the filename so it doesn't break the 'width' integer ---
    generate_julia(c_const, filename="static/latest_fractal.png")
    
    actual_freq = generate_weather_tone(wind)
    
    history = []
    if os.path.exists("static/weather_stats.json"):
        try:
            with open("static/weather_stats.json", "r") as f:
                old_data = json.load(f)
                history = old_data.get("history", [])
        except:
            pass

    history.insert(0, {"time": last_update, "temp": temp})
    history = history[:5]
    
    stats = {
        "last_update": last_update,
        "temp": temp, 
        "humidity": humidity, 
        "wind": wind,
        "freq": round(actual_freq, 2) if actual_freq is not None else 0,
        "c_real": round(c_const.real, 4), 
        "c_imag": round(c_const.imag, 4),
        "history": history
    }

    with open("static/weather_stats.json", "w") as f:
        json.dump(stats, f)
    
    print(f"Success: Updated fractal and audio for {temp}°C at {last_update}")

if __name__ == "__main__":
    main()