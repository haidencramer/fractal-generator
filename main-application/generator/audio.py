import numpy as np
from scipy.io import wavfile

import matplotlib
matplotlib.use('Agg')  # Prevents crashes on headless servers
import matplotlib.pyplot as plt  # This defines 'plt'
import numpy as np
from scipy.io import wavfile

def generate_weather_tone(wind_speed, filename="static/latest_audio.wav"):
    # Calculate freq first to avoid previous NameErrors
    freq = 200 + (float(wind_speed) * 50)
    
    sample_rate = 44100
    duration = 3.0
    t = np.linspace(0, duration, int(sample_rate * duration))
    
    # Generate the audio signal
    audio = 0.5 * np.sin(2 * np.pi * freq * t)
    
    # Save the WAV file
    wavfile.write(filename, sample_rate, (audio * 32767).astype(np.int16))
    
    # Now plt will work!
    plt.figure(figsize=(10, 4), facecolor='black')
    plt.specgram(audio, Fs=sample_rate, cmap='inferno')
    plt.axis('off')
    plt.savefig("static/spectrogram.png", bbox_inches='tight', pad_inches=0, transparent=True)
    plt.close()
    
    return freq