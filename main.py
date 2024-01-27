import weather #retrieves info about the weather
import tkinter #allows us to make graphical apps with python


#define window
mainWindow = tkinter.Tk()
#size of our application
mainWindow.geometry("300x300")
#title your app
mainWindow.title("weather app by chantelle")
#color our backround
mainWindow.config(bg="#CDA8FF")
#acessing our weather info
api_key="1cc72f37ccff0068813610aa29f347d3"

title = tkinter.Label(text="Weather app",
   bg=mainWindow['bg'],
   font=('DejaVu Serif',20,'italic'),
   fg="#F7FEAB")

title.pack(pady=20)

countryPrompt = tkinter.Label(text="Country: ",bg=mainWindow['bg'])
countryPrompt.pack()

countryBox = tkinter.Entry()
countryBox.pack(pady=5)

cityPrompt = tkinter.Label(text="City: ",bg=mainWindow['bg'])
cityPrompt.pack()

cityBox = tkinter.Entry()
cityBox.pack(pady=5)

def getWeather():
  city = cityBox.get()
  country = countryBox.get()
  temperature = weather.get_weather(city, country, api_key)
  if temperature:
    result.config(text=f"The temperature in {city}, {country} is {round(temperature)}°C.")
  else:
    result.config(text="Tempature unavailible")












button = tkinter.Button(text="Get Weather",command=getWeather)
button.pack(pady=5)

result = tkinter.Label(text="",bg=mainWindow['bg'],font=("Arial",10,"italic"))
result.pack(pady=10)






#run our code
mainWindow.mainloop()
