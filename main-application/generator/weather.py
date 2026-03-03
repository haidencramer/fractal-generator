import requests

def get_weather_data(lat=46.8721, lon=-113.9940):
    """
    Fetches real-time weather data for a specific location.
    Default coordinates: Missoula, MT.
    """
    url = "https://api.open-meteo.com/v1/forecast"
    
    # We request temperature for the fractal and wind speed for the audio
    params = {
        "latitude": lat,
        "longitude": lon,
        "current": ["temperature_2m", "relative_humidity_2m", "wind_speed_10m"],
        "timezone": "auto"
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status() # Raises an error for bad status codes
        
        data = response.json()
        current = data.get("current", {})

        # Extract the specific metrics we need for seeding our art
        return {
            "temp": current.get("temperature_2m", 0),
            "humidity": current.get("relative_humidity_2m", 0),
            "wind": current.get("wind_speed_10m", 0),
            "units": {
                "temp": "C",
                "wind": "km/h"
            }
        }
    except Exception as e:
        print(f"Error fetching weather: {e}")
        # Return fallback data so the pipeline doesn't crash
        return {"temp": 20, "humidity": 50, "wind": 10}

if __name__ == "__main__":
    # Test run
    print("Testing Weather Fetch...")
    print(get_weather_data())