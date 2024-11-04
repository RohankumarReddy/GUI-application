import tkinter as tk
import requests

HEIGHT = 500
WIDTH = 600

def format_response(weather):
    try:
        name = weather['name']
        description = weather['weather'][0]['description']
        temp = weather['main']['temp']
        # Format the display string
        final_str = f"City: {name}\nCondition: {description}\nTemperature: {temp}°C"
    except KeyError:
        final_str = "Error retrieving weather data."
    
    return final_str

def get_weather(city):
    weather_key = '1c8c3e5413827eecbf617b4f9a64494b'
    link = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'metric'}
    response = requests.get(link, params=params)
    
    if response.status_code == 200:
        weather = response.json()
        label['text'] = format_response(weather)
    else:
        label['text'] = "City not found. Please try again."

root = tk.Tk()
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_img = tk.PhotoImage(file='images/red.png')
background = tk.Label(root, image=background_img)
background.place(x=0, y=0, relheight=1, relwidth=1)

frame = tk.Frame(root, bg='#5fff5a', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Forecast", font=40, command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg='#5fff5a', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, bg='white', bd=5, font=("Helvetica", 30), anchor="nw", justify="left")
label.place(relheight=1, relwidth=1)

root.mainloop()
