import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile

def generate_weather_tone(wind_speed, filename="static/latest_audio.wav"):
    # Base frequency from wind
    freq = 200 + (float(wind_speed) * 50)
    sample_rate = 44100
    duration = 5.0  # Slightly longer for a better drone
    t = np.linspace(0, duration, int(sample_rate * duration))
    
    # Create a Rich Drone: Fundamental + Harmonics + "Gust" modulation
    # This sounds like a flute or wind instrument instead of a PC beep
    gust = 0.6 + 0.4 * np.sin(2 * np.pi * 0.3 * t) 
    audio = (0.5 * np.sin(2 * np.pi * freq * t) + 
             0.2 * np.sin(2 * np.pi * (freq * 1.5) * t) + 
             0.1 * np.sin(2 * np.pi * (freq * 2) * t)) * gust
    
    # Save Audio
    wavfile.write(filename, sample_rate, (audio * 32767).astype(np.int16))
    
    # Create a "Cooler" Spectrogram
    plt.figure(figsize=(12, 5), facecolor='black')
    plt.specgram(audio, Fs=sample_rate, cmap='magma', NFFT=1024) # 'magma' is deep purple/orange
    plt.axis('off')
    # Save to static folder
    plt.savefig("static/spectrogram.png", bbox_inches='tight', pad_inches=0, transparent=True, dpi=150)
    plt.close()
    
    return freq