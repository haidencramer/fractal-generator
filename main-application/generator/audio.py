import numpy as np
from scipy.io import wavfile

def generate_weather_tone(wind_speed, filename="static/latest_audio.wav"):
    sample_rate = 44100
    duration = 5.0
    # Map wind speed (typically 0-30km/h) to frequency (220-700Hz)
    frequency = 220 + (wind_speed * 15)
    
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    tone = np.sin(frequency * t * 2 * np.pi)
    
    # Standardize to 16-bit integer for WAV file compatibility
    final_audio = (tone * 32767).astype(np.int16)
    wavfile.write(filename, sample_rate, final_audio)