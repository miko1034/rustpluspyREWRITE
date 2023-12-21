from tkinter import *

def gui():
    #window
    window = Tk()
    window.geometry("500x500")
    #frames
    mainframe = Frame(window)
    #frames pack
    mainframe.pack()
    mainframe.pack_propagate(False)
    mainframe.configure(width=500,height=500)
    mainframe.mainloop()

gui()