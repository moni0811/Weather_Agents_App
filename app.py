#app.py

import streamlit as st
from agents import coordinator

st.title("Multi-Agent Weather App")

city = st.text_input("Enter City Name")
api_key = st.text_input("Enter OpenWeatherMap API Key", type="password")

if st.button("Get Weather"):
    if city and api_key:
        try:
            weather_data, chart = coordinator(city, api_key)

            # Check for errors
            if "error" in weather_data:
                st.error(f"Error fetching weather data: {weather_data['error']}")
            else:
                # Display basic weather info instead of full JSON
                st.subheader(f"Weather for {city}")

                if 'list' in weather_data and len(weather_data['list']) > 0:
                    current = weather_data['list'][0]
                    temp_celsius = current['main']['temp'] - 273.15
                    feels_like = current['main']['feels_like'] - 273.15
                    humidity = current['main']['humidity']
                    description = current['weather'][0]['description']

                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("Temperature", f"{temp_celsius:.1f}°C")
                    with col2:
                        st.metric("Feels Like", f"{feels_like:.1f}°C")
                    with col3:
                        st.metric("Humidity", f"{humidity}%")

                    st.write(f"**Condition:** {description.title()}")

                # Display chart
                if chart:
                    st.subheader("24-Hour Temperature Forecast")
                    st.image(f"data:image/png;base64,{chart}")
                else:
                    st.error("Failed to generate chart")

                # Show raw JSON in an expandable section
                with st.expander("View Raw Weather Data"):
                    st.json(weather_data)

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            st.write("Please check your API key and city name.")
    else:
        st.warning("Please enter both city name and API key.")
