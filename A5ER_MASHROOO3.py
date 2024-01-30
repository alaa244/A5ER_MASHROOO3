import tkinter as tk
from tkinter import messagebox
import requests

def get_weather(city, api_key="80c703d08526f0cee557a12c969bfdfb"):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        response.raise_for_status()  
        weather_data = response.json()
        return weather_data
    except requests.exceptions.RequestException as e:
        print(f"Error making request: {e}")
        return None

def display_weather():
    city = entry_city.get()
    api_key = "80c703d08526f0cee557a12c969bfdfb"  

    if not city:
        messagebox.showerror("Error", "Please enter a city name.")
        return

    button_get_weather.config(state=tk.DISABLED) 

    weather_data = get_weather(city, api_key)

    button_get_weather.config(state=tk.NORMAL)  

    if weather_data:
        print("Weather Data:", weather_data)

        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']
        rain_probability = weather_data.get('rain', {'1h': 0}).get('1h', 0)
        pressure = weather_data['main']['pressure']

        result_text = f"Temperature: {temperature:.2f} °C\n\n"
        result_text += f"Humidity: {humidity:.2f}%\n\n"
        result_text += f"Wind Speed: {wind_speed:.2f} km/h\n\n"
        result_text += f"Rain Probability: {rain_probability:.2f}%\n\n"
        result_text += f"Pressure: {pressure:.2f} hPa"

        label_result.config(text=result_text)
    else:
        messagebox.showerror("Error", "Failed to retrieve weather information.")

app = tk.Tk()
app.title("WEATHER FORECAST")

label_city = tk.Label(app, text="City:")


entry_city = tk.Entry(app)
entry_city.pack(pady=10)

button_get_weather = tk.Button(app, text="Get Weather Information", command=display_weather)
button_get_weather.pack(pady=20)

label_result = tk.Label(app, text="")
label_result.pack()

app.mainloop()
