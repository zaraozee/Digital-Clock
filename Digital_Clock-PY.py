from tkinter import Tk, Label
import time

master = Tk()
master.title("Digital Clock")

def get_time():
    timeVar = time.strftime("%I:%M:%S %p")
    clock.config(text=timeVar)
    clock.after(200, get_time)

clock = Label(master, font=("Stencil", 90, "bold"), bg="black", fg="sky blue", bd=30, relief="sunken")
clock.pack()

get_time()

master.mainloop()