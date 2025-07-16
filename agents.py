#agents.py

from utils import get_weather, plot_temperature
import streamlit as st


def weather_agent(city, api_key):
    weather_data = get_weather(city, api_key)
    return weather_data


def chart_agent(weather_data):
    return plot_temperature(weather_data)


def coordinator(city, api_key):
    weather_data = weather_agent(city, api_key)

    # Check if there's an error in weather data
    if "error" in weather_data:
        return weather_data, None

    try:
        chart = chart_agent(weather_data)
        return weather_data, chart
    except Exception as e:
        # Display the actual error for debugging
        st.error(f"Error generating chart: {str(e)}")
        return weather_data, None
