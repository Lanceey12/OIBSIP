from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root = tk.Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)


def get_weather():
    city = textfield.get()

    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(city)
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M %p")
    clock.config(text=current_time)
    name.config(text="Current Weather")

    url = url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=<apikey>"
    json_data = requests.get(url).json()
    condition = json_data['weather'][0]['main']
    description = json_data['weather'][0]['description']
    temp = int(json_data['main']['temp']-273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']

    t.config(text=f"{temp}°")
    c.config(text=f"{condition} | FEELS LIKE {temp}°")
    w.config(text=f"Wind Speed: {wind} m/s")
    h.config(text=f"Humidity: {humidity}%")
    d.config(text=f"Description: {description}")
    p.config(text=f"Pressure: {pressure} hPa")


search_image = PhotoImage(file="copy of search.png")
myimage_label = Label(image=search_image)
myimage_label.place(x=20, y=20)

textfield = tk.Entry(root, justify="center", width=17, font=("Bebas kai", 25, "bold"), bg="#404040",
                     fg="Black", border=0)
textfield.place(x=50, y=40)
textfield.focus()

search_icon = PhotoImage(file="copy of search_icon.png")
myimage_icon = Button(image=search_icon, borderwidth=0, cursor="hand2", command=get_weather)
myimage_icon.place(x=400, y=34)

Logo_image = PhotoImage(file="copy of logo.png")
logo = Label(image=Logo_image)
logo.place(x=150, y=100)

Frame_image = PhotoImage(file="copy of box.png")
frame_myimage = Label(image=Frame_image)
frame_myimage.pack(padx=5, pady=5, side=BOTTOM)

name = Label(root, font=("Bebas kai", 15, "bold"))
name.place(x=30, y=100)
clock = Label(root, font=("Bebas kai", 20))
clock.place(x=30, y=130)

label1 = Label(root, text="Wind Speed", font=("Bebas kai", 15, "bold"), fg="white")
label1.place(x=120, y=400)

label2 = Label(root, text="Humidity", font=("Bebas kai", 15, "bold"), fg="white")
label2.place(x=250, y=400)

label3 = Label(root, text="Description", font=("Bebas kai", 15, "bold"), fg="white")
label3.place(x=430, y=400)

label4 = Label(root, text="Pressure", font=("Bebas kai", 15, "bold"), fg="white")
label4.place(x=650, y=400)

t = Label(font=("Bebas kai", 70, "bold"), fg="Blue")
t.place(x=400, y=150)

c = Label(font=("Bebas kai", 15, "bold"))
c.place(x=400, y=250)

w = Label(font=("Bebas kai", 15), bg="#1ab5ef")
w.place(x=120, y=430)

h = Label(font=("Bebas kai", 15), bg="#1ab5ef")
h.place(x=280, y=430)

d = Label(font=("Bebas kai", 15), bg="#1ab5ef")
d.place(x=450, y=430)

p = Label(font=("Bebas kai", 15), bg="#1ab5ef")
p.place(x=670, y=430)

root.mainloop()
