# 🌦️ Weather Voice Assistant in Python

This Python project is a **command-line weather assistant** that fetches live weather data using the [WeatherAPI](https://www.weatherapi.com/) and reads it aloud using **text-to-speech (TTS)**. It's like having your own Jarvis that tells you what the weather is like.

---

## 🚀 Features

- 🔎 Fetches **live weather** using city name
- 🗣️ Reads the weather out loud using `pyttsx3` (cross-platform TTS)
- 🌡️ Shows:
  - Temperature and "feels like"
  - Weather condition (Sunny, Rain, etc.)
  - Wind speed & direction
  - Humidity & visibility
  - Pressure & UV index
  - Rainfall & cloud coverage
- 🛡️ Handles errors gracefully (e.g., invalid city)

---

## 📦 Requirements

- Python 3.6+
- Install the required modules:
  ```bash
  pip install requests pyttsx3
