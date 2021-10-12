import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mbox
import requests
import json, base64
from typing import Sized

api_key = "7a94044a978f9efaeb198935f60f4280"
base_url = "http://api.openweathermap.org/data/2.5/weather?"



def findweather():
    city_name = city.get()  #getting value
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name  #request url
    response = requests.get(complete_url)  #sending request
    x = response.json()
    print(x)

    if x["cod"] != "404":
        y = x['main']
        temp_kelvin = y['temp']
        temp = str(temp_kelvin-275.15)[0:2]

        humidity = y['humidity']

        z = x['weather']
        weather_disc = z[0]["description"]

        mbox.showinfo("Weather", f"Temperature : {temp} °C\nhumidity : {humidity} %\nDescription :  : {weather_disc}")
        # current_temp = ttk.Label(root, text=f"Current temperature : {temp} °C  ")
        # current_temp.place(x = 70, y = 150)
        # current_humidity = ttk.Label(root, text=f"Current humidity : {humidity} %")
        # current_humidity.place(x = 70, y = 170)
        # current_temp = ttk.Label(root, text=f"Description :  : {weather_disc}")
        # current_temp.place(x = 70, y = 190)

    else:
        mbox.showerror("Error",f"Not Valid City\nPlease check again!")
        # error_win.place(x = 70, y = 150)
        # error_win.config(fg= "red")



root  = tk.Tk()
root.geometry('450x250+550+250')
root.title("Weather App")
tit_le = ttk.Label(root, text="Enter City : ", font=('Helvetica', 20,))
tit_le.place(x=70, y=40)
city = ttk.Entry(root)
city.place(x=70, y=100)
city.focus()
cta_button = ttk.Button(root, text="Submit", command=findweather)
cta_button.place(x=260, y=100)

root.mainloop()


