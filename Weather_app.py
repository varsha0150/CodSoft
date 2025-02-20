import requests
import tkinter as tk
from tkinter import messagebox

API_KEY = "f4d60fe664c8959a48cac33afacea83e"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# Function to fetch weather data
def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showerror("Error", "Please enter a city name.")
        return
    
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    
    if response.status_code == 200:
        city_name = data["name"]
        country = data["sys"]["country"]
        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"]

        result_label.config(text=f"🌍 {city_name}, {country}\n🌡 Temperature: {temp}°C\n🌥 Weather: {weather.capitalize()}")
    else:
        messagebox.showerror("Error", "City not found. Please enter a valid city.")


root = tk.Tk()
root.title("Weather App by Varsha")
root.geometry("350x300")
root.configure(bg="lightblue")


tk.Label(root, text="Enter City:", font=("Arial", 15 , "bold"), bg="lightblue", fg ="#010057").pack(pady=10)
city_entry = tk.Entry(root, font=("Arial", 14),bg = "#fff7e1", width=20)
city_entry.pack()

tk.Button(root, text="Get Weather", font=("Arial", 12),bg="#84cdee", command=get_weather).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14 , "bold"), bg="lightblue", fg ="#010057" , justify="center")
result_label.pack(pady=20)


root.mainloop()
