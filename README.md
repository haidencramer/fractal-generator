# Atmospheric Julia Set Observer
**Midterm Project: Cloud-Native Architecture (Track C: The Observer)**

An automated data pipeline that fetches real-time weather data from Missoula, MT, to drive a complex mathematical visualization and audio sonification engine.

## Infrastructure and DevOps
- **Secured Perimeter:** Principle of Least Privilege enforced via Jetstream2 firewall (Only Ports 22, 80, 443 open).
- **GitOps Automation:** Continuous Deployment via GitHub Actions (deploy.yml) on every push to main.
- **Multi-Tenant Routing:** Served over HTTPS via Caddy with a custom .nip.io subdomain.
- **Resilience:** Background tasks managed by systemd. A Systemd Timer runs the observer hourly, and the FastAPI app is managed as a persistent service.

## How it Works
1. **The Observer:** A Python script triggers hourly to fetch Temperature, Humidity, and Wind Speed from the Open-Meteo API.
2. **The Math:** Weather variables are mapped to the Complex Constant 'c' in the Julia Set equation: z(n+1) = z(n)^2 + c.
3. **The Sonification:** Wind speed drives a sine-wave oscillator in the backend, generating a .wav file and a spectrogram PNG representing the "sonic signature" of the wind.
4. **The UI:** A high-iteration Canvas frontend allows users to explore the fractal with weather-driven focus points.

## Obstacles Overcome
- **Type Handling:** Resolved NoneType and NameError bugs in the data pipeline to ensure 100% uptime.
- **Headless Plotting:** Implemented the 'Agg' backend for Matplotlib to allow spectrogram generation on a server without a display.
- **Dynamic Targeting:** Built a targeting algorithm so the auto-zoom hunts for detail based on weather instead of empty space. 