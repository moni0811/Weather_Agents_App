#utils.py

import matplotlib.pyplot as plt
import io
import base64
import requests
import pandas as pd
import urllib3
from datetime import datetime

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def plot_temperature(weather_data):
    # Extract temperature data from OpenWeatherMap API response
    forecast_list = weather_data.get('list', [])

    if not forecast_list:
        raise ValueError("No forecast data available")

    # Process the data to extract hour and temperature
    processed_data = []
    start_time = None

    for i, item in enumerate(forecast_list):
        dt = datetime.fromtimestamp(item['dt'])

        # Set start time from first entry
        if start_time is None:
            start_time = dt

        # Only include data points within 24 hours from start
        time_diff = (dt - start_time).total_seconds() / 3600  # Convert to hours
        if time_diff > 24:
            break

        # Format time display
        hour = dt.strftime('%H:%M')
        date_str = dt.strftime('%m/%d')

        # Extract temperature (convert from Kelvin to Celsius)
        temp = item['main']['temp'] - 273.15

        processed_data.append({
            'hour': hour,
            'date': date_str,
            'temp': round(temp, 1),
            'datetime': dt
        })

    # Ensure we have exactly 24 hours or less
    if len(processed_data) > 9:  # OpenWeatherMap gives data every 3 hours, so 8 points = 24 hours
        processed_data = processed_data[:9]

    # Create DataFrame from processed data
    df = pd.DataFrame(processed_data)

    # Create matplotlib chart
    plt.figure(figsize=(14, 6))
    plt.plot(range(len(df)), df['temp'], color='#FF6B6B', linewidth=2, marker='o', markersize=6)
    plt.title('Temperature Forecast (24 hours)', fontsize=16, fontweight='bold')
    plt.xlabel('Time', fontsize=12)
    plt.ylabel('Temperature (°C)', fontsize=12)
    plt.grid(True, alpha=0.3)

    # Set x-axis labels to show time and date
    x_labels = []
    for i, row in df.iterrows():
        if i == 0 or row['date'] != df.iloc[i - 1]['date']:
            x_labels.append(f"{row['hour']}\n{row['date']}")
        else:
            x_labels.append(row['hour'])

    plt.xticks(range(len(df)), x_labels, rotation=0)
    plt.tight_layout()

    # Convert to base64 image
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png', dpi=300, bbox_inches='tight')
    buffer.seek(0)
    img_base64 = base64.b64encode(buffer.getvalue()).decode()
    plt.close()  # Close the figure to free memory

    return img_base64


def get_weather(city: str, api_key: str):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}"
    try:
        response = requests.get(url, verify=False)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
