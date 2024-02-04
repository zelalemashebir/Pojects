

from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime 
import requests
import pytz

root=Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False,False)


def getWeather():
    city=textfield.get()

    geolacator=Nominatim(user_agent="geoapi_Excersice")
    location=geolacator.deocode(city)
    obj=TimezoneFinder()
    result=obj.timezone_at(lng=location.longitude,lat=location.latitude)
    
    home=pytz.timezone(result)
    local_time=datetime.now(home)
    currenttime=local_time.strftime("%I:%M %P")


#searchbox
Search_image=PhotoImage(file="search.PNG" )
myimage=Label(image=Search_image)
myimage.place(x=20,y=20)

textfield=tk.Entry(root,justify="center",width=17,font=("poppins",25,"bold"),bg="#404040", border=0,fg="white")
textfield.place(x=50,y=40)
textfield.focus()

Search_icon=PhotoImage(file="search_icon.PNG")
myimage_icon=Button(image=Search_icon,borderwidth=0,cursor="hand2",bg="#404040",border=0, command=getWeather)
myimage_icon.place(x=400,y=34)


#logo
Logo_image=PhotoImage(file="logo.png")
logo_img=Label(image=Logo_image)
logo_img.place(x=150,y=100)


#btmBox
Frame_image=PhotoImage(file="box.png")
frame_myimg=Label(image=Frame_image)
frame_myimg.pack(padx=5,pady=5,side=BOTTOM)

#time
name=Label(root,font=("aerial",15,"bold"))
name.place(x=20 ,y=20)



#label
label1=Label(root,text="WIND",font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
label1.place(x=120,y=400)

label2=Label(root,text="HUMIDITY",font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
label2.place(x=250,y=400)

label3=Label(root,text="DESCRIPTION",font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
label3.place(x=430,y=400)

label4=Label(root,text="PRESSUE",font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
label4.place(x=650,y=400)


t=Label(font=("aerial",70,"bold"),fg="#ee666d")
t.place(x=400,y=150)
c=Label(font=("aerial",15,"bold"))
c.place(x=400,y=250)

w=Label(text="...", font =("aerial",20,"bold"),bg="#1ab5ef")
w.place(x=120,y=430)
h=Label(text="...", font =("aerial",20,"bold"),bg="#1ab5ef")
h.place(x=280,y=430)
d=Label(text="...", font =("aerial",20,"bold"),bg="#1ab5ef")
d.place(x=450,y=430)
p=Label(text="...", font =("aerial",20,"bold"),bg="#1ab5ef")
p.place(x=670,y=430)






root.mainloop()


