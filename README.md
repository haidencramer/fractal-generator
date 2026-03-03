# Generative Fractal Observer

## Project Track
**Track C: The Observer (Automated Data Pipeline)**

## Project Description
For my midterm project, I plan to build a cloud-native system on Jetstream2 that translates real-time weather conditions into fractal like art and audio. 

The goal is to create an observer pipeline that runs independently from the server. Every hour, I plan on using a background task to fetch local weather data in Missoula, Montana(temperature, humidity, and wind speed) from a public API. This data will be used as a "seed" for two processes I would like to explore:

1.  **Fractal Generation:** A Python script will render a Julia Set fractal where the visual is determined by current temperature and humidity for the constants within the equation.
2.  **Audio Synthesis:** The system will generate a short ambient audio loop where the frequency/pitch is influenced by current wind speeds. (Probably not gonna sound good but very curious idea)

The application will be served via a FastAPI dashboard behind a Caddy reverse proxy on a .nip.io subdomain like we have done in class. I also intend to use systemd timers to ensure the data collection is consistent across reboots.

## Planned Tech Stack
* **Language:** Python
* **Infrastructure:** Jetstream2
* **Process Management:** systemd (Services and Timers)
* **Web Server:** FastAPI and Caddy
* **Deployment:** GitHub Actions (CI/CD)