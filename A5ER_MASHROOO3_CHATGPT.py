import tkinter as tk
from tkinter import messagebox
import requests

# Function to get weather data from OpenWeatherMap API
def get_weather(city, api_key="80c703d08526f0cee557a12c969bfdfb"):
    # Construct the API request URL
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        # Make the API request and handle exceptions
        response = requests.get(url)
        response.raise_for_status()  
        weather_data = response.json()
        return weather_data
    except requests.exceptions.RequestException as e:
        # Print an error message if the request fails
        print(f"Error making request: {e}")
        return None

# Function to display weather information on the GUI
def display_weather():
    # Get the city name and API key from the user input
    city = entry_city.get()
    api_key = "80c703d08526f0cee557a12c969bfdfb"  

    # Check if the city name is provided
    if not city:
        # Show an error message if the city name is missing
        messagebox.showerror("Error", "Please enter a city name.")
        return

    # Disable the button during the API request to avoid multiple requests
    button_get_weather.config(state=tk.DISABLED) 

    # Get weather data for the specified city
    weather_data = get_weather(city, api_key)

    # Enable the button after the API request is complete
    button_get_weather.config(state=tk.NORMAL)  

    # Check if weather data is retrieved successfully
    if weather_data:
        print("Weather Data:", weather_data)

        # Extract relevant weather information
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']
        rain_probability = weather_data.get('rain', {'1h': 0}).get('1h', 0)
        pressure = weather_data['main']['pressure']

        # Format the result text to display on the GUI
        result_text = f"Temperature: {temperature:.2f} °C\n\n"
        result_text += f"Humidity: {humidity:.2f}%\n\n"
        result_text += f"Wind Speed: {wind_speed:.2f} km/h\n\n"
        result_text += f"Rain Probability: {rain_probability:.2f}%\n\n"
        result_text += f"Pressure: {pressure:.2f} hPa"

        # Update the label with the result text
        label_result.config(text=result_text)
    else:
        # Show an error message if weather data retrieval fails
        messagebox.showerror("Error", "Failed to retrieve weather information.")

# Create the main Tkinter application window
app = tk.Tk()
app.title("WEATHER FORECAST")

# Create and place GUI elements (labels, entry, button, and result label)
label_city = tk.Label(app, text="City:")
label_city.pack(pady=10)

entry_city = tk.Entry(app)
entry_city.pack(pady=10)

button_get_weather = tk.Button(app, text="Get Weather Information", command=display_weather)
button_get_weather.pack(pady=20)

label_result = tk.Label(app, text="")
label_result.pack()

# Start the Tkinter main loop
app.mainloop()
