# Weather_Agents_App

This is a modular, agent-driven Streamlit application that fetches and visualizes 24-hour weather forecasts for any city using the OpenWeatherMap API.

## 🚀 Features

- 🔍 **Modular agent-based architecture**
- 🌡️ Fetches real-time weather data
- 📊 Visualizes temperature trends for next 24 hours
- 🛡️ API key protected
- 🧰 Expandable raw JSON output for dev/debug

## 🧱 Project Structure

├── app.py # Streamlit frontend
├── agents.py # Agent functions (weather fetch, chart gen, coordinator)
├── utils.py # Utilities for fetching data & generating charts


## 🖥️ How It Works

1. User enters:
   - City name
   - OpenWeatherMap API key
2. App fetches and processes weather forecast
3. Displays:
   - Current weather conditions
   - Line chart showing 24-hour temperature trend
   - Optional raw data

## 🧪 Local Setup

```bash
git clone https://github.com/moni0811/weather_agents_app.git
cd weather_agents_app
streamlit run app.py
```

## Get Your API Key
1. Go to OpenWeatherMap
2. Sign up and generate an API key
3. Paste it into the app when prompted

## 📦 Requirements
streamlit
matplotlib
pandas
requests




