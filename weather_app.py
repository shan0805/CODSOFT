import tkinter as tk
import requests


API_KEY = '30d4741c779ba94c470ca1f63045390a'

def get_weather():
    city = city_entry.get()
    weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={API_KEY}")
    
    if weather_data.json()['cod'] == '404':
        result_label.config(text="No City Found", fg='red')
    else:
        weather = weather_data.json()['weather'][0]['main']
        temp = round(weather_data.json()['main']['temp'])
        humidity = weather_data.json()['main']['humidity']
        result_label.config(text=f"The weather in {city} is: {weather}\n"
                                 f"The temperature in {city} is: {temp}ºF\n"
                                 f"The humidity in {city} is: {humidity}%", fg='black')

# GUI Setup
root = tk.Tk()
root.title("Weather App")

# Calculate the position to center the window
window_width = 400
window_height = 200
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_position = (screen_width // 2) - (window_width // 2)
y_position = (screen_height // 2) - (window_height // 2)

# Set the window size and position
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# Adding an attractive background color
root.config(bg="white")

city_label = tk.Label(root, text="Enter city:", font=("Helvetica", 14), bg="white")
city_label.pack()

city_entry = tk.Entry(root, width=30, font=("Helvetica", 12))
city_entry.pack()

get_weather_button = tk.Button(root, text="Get Weather", command=get_weather, font=("Helvetica", 12), bg="grey", fg="white")
get_weather_button.pack()

result_label = tk.Label(root, text="", font=("Helvetica", 14), bg="white")
result_label.pack()

root.mainloop()
