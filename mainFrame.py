from tkinter import *
import tkinter as tk
from tkinter import ttk
from connector import *
from tkinter import font as tkfont
from PIL import Image, ImageTk
from connector2 import *
from dashboardPage import *

class mainFrame(tk.Tk):
    """
    Frame object holding all of the different pages
    Controller of my pages
    """
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        
        self.titlefont = tkfont.Font(family="Verdana", size = 12, weight = "bold", slant='roman')
        self.title("SIBUKIN")
        image_icon = PhotoImage(file="image/list.png")
        self.iconphoto(False, image_icon)
        self.container = tk.Frame()
        self.container.pack(side='top', fill='both',expand=True)
        self.container.grid_rowconfigure(0, weight = 1)
        self.container.grid_columnconfigure(0, weight = 1)

        self.id = tk.StringVar()
        self.id.set('Wipiii')

        self.listFrame = {}

        for page in (dashboardPage, PageOne):
            page_name = page.__name__
            frame = page(parent = self.container, controller = self)
            frame.grid(row=0, column=0, sticky='nsew')
            self.listFrame[page_name] = frame

        self.up_frame('PageOne')
    
    def up_frame(self, selectedPage):
        page = self.listFrame[selectedPage]
        # page.refetchdata()
        page.tkraise()

    # def navbar(self):
    #     self.header = Frame(self, background="White", height = 100)
    #     self.header.pack(fill=X)


class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.id = controller.id

        label = tk.Label(self,text="PageOne \n" + controller.id.get(),font= controller.titlefont)

        label.pack()

        bou = tk.Button(self, text="back to dashboard page", command= lambda: controller.up_frame("dashboardPage"))
        bou.pack()

if __name__ == '__main__':
    app = mainFrame()
    app.mainloop()