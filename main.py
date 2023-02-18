import tkinter as tk
import customtkinter
import requests
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")
class WeatherApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Weather App")

        self.label = customtkinter.CTkLabel(self.master, text="Enter City Name:")
        self.label.pack(pady=12, padx=10)

        self.city_entry = customtkinter.CTkEntry(self.master, width=100)
        self.city_entry.pack(pady=12, padx=10)

        self.get_weather_button = customtkinter.CTkButton(self.master, text="Get Weather", command=self.get_weather)
        self.get_weather_button.pack(pady=12, padx=10)

        self.temperature_label = customtkinter.CTkLabel(self.master, text="")
        self.temperature_label.pack(pady=12, padx=10)

        self.description_label = customtkinter.CTkLabel(self.master, text="")
        self.description_label.pack(pady=12, padx=10)

    def get_weather(self):
        city = self.city_entry.get()

        # OpenWeatherMap API
        # url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOUR_OPENWEATHERMAP_API_KEY&units=metric'
        # response = requests.get(url)
        # data = response.json()

        # WeatherBit API
        url = f'https://api.weatherbit.io/v2.0/current?city={city}&key=3565a4cd2d584e929be58a0df261d17b&units=M'
        response = requests.get(url)
        data = response.json()

        if 'data' in data:
            temperature = data['data'][0]['temp']
            description = data['data'][0]['weather']['description']
            self.temperature_label.configure(text=f'Temperature: {temperature}°C')
            self.description_label.configure(text=f'Weather Description: {description}')
        else:
            self.temperature_label.configure(text='Unable to retrieve weather information')
            self.description_label.configure(text='')


root = customtkinter.CTk()
root.geometry("300x350")
weather_app = WeatherApp(root)
root.mainloop()



