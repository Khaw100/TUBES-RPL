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
        # self.geometry("800x800")
        self.container = tk.Frame()
        self.container.pack(side='top', fill='both',expand=True)
        # self.container.grid(row = 0, column = 0, sticky ="nesw")
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

        self.up_frame('dashboardPage')
    
    def up_frame(self, selectedPage):
        page = self.listFrame[selectedPage]
        # page.refetchdata()
        page.tkraise()

    # def navbar(self):
    #     self.header = Frame(self, background="White", height = 100)
    #     self.header.pack(fill=X)


# class dashboardPage(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         self.controller = controller
#         self.id = controller.id

#         #===================================================================================================================================================================#

#         self.activityID = IntVar()
#         self.activityName = StringVar()
#         self.categoryName = StringVar()
#         self.deadline = StringVar()
#         self.status = StringVar()

#         self.clicked = StringVar()

#         #=========================================================================FRAME=====================================================================================#
#         # Central Frame
#         self.centralframe = Frame(self, background="white")
#         self.centralframe.pack(ipady=700, ipadx=700)

#         # Label Title
#         self.labelTitle = Label(self.centralframe, text="SIBUKIN", background="white", borderwidth=0, fg="BLACK",font=('times new roman',50,'bold'))
#         self.labelTitle.pack(side=TOP, fill=X)

#         # Button Frame
#         self.buttonFrame = Frame(self.centralframe, background="white")
#         self.buttonFrame.pack(anchor="center", pady=40)

#         # Table Frame
#         self.tableframe = Frame(self.centralframe, background="white", highlightbackground="black", highlightthickness=2)
#         self.tableframe.pack(anch='center')

#         ## , highlightbackground="black", highlightthickness=2

#         #=========================================================================BUTTON==================================================================================#

#         self.buttonFilter = Button(self.buttonFrame, text = "Filter", width=23, height =2, padx =2)
#         # self.buttonFilter.grid(row=0, column=2)
#         self.buttonFilter.pack(side = RIGHT, padx = 15)

#         self.buttonTambahKategori = Button(self.buttonFrame, text = "+ Tambah Kategori", width=23, height =2, padx =2)
#         # self.buttonTambahKategori.grid(row=0, column=1)
#         self.buttonTambahKategori.pack(side = RIGHT, padx = 15)

#         self.buttonTambahKegiatan = Button(self.buttonFrame, text = "+ Tambah Kegiatan", command = self.popupActivity, width=23, height =2, padx =2)
#         # self.buttonTambahKegiatan.grid(row=0, column=9)
#         self.buttonTambahKegiatan.pack(side = RIGHT, padx = 15)

#         #===========================================================================TABLE==================================================================================#
#         scroll_y = ttk.Scrollbar(self.tableframe, orient=VERTICAL)
#         self.todolistTable = ttk.Treeview(self.tableframe, columns=(1,2,3,4,5), show="headings", height="24", yscrollcommand=scroll_y.set)
#         scroll_y.pack(side=RIGHT, fill = Y)
#         scroll_y = ttk.Scrollbar(command=self.todolistTable.yview)
#         self.todolistTable.column(1, minwidth=0, width =0, stretch=NO)
#         self.todolistTable.heading(1, text="idKegiatan")
#         self.todolistTable.heading(2, text="Activity Name")
#         self.todolistTable.heading(3, text="Category Name")
#         self.todolistTable.heading(4, text="Deadline")
#         self.todolistTable.heading(5, text="Status")

#         self.todolistTable['show']='headings'
#         self.todolistTable.pack(fill=BOTH, expand=1)
#         # self.buttonFrame.place(y=100, width=300, height=50)
#         # label = tk.Label(self,text="Dashboard page \n" + controller.id.get(),font= controller.titlefont, highlightbackground="yellow", highlightthickness=2)
#         # label.pack()
#         # bou = tk.Button(self, text="to next page", command= lambda: controller.up_frame("PageOne"))
#         # bou.pack()

#     #========================================================================OTHER FUNCTION==========================================================================#
#     def fetchTodayData(self):
#         self.konektor = connector("localhost", "wipiii", "miscrit10", "rpl")
#         self.konektor.openConnection()

#         self.konektor.allToDoList()

#     def popupActivity(self):

#         #========================Make The Pop Up Windows Position At The Center=================================#
#         # Get main window position
#         root_x = self.winfo_rootx()
#         root_y = self.winfo_rooty()

#         # Add Offset
#         win_x = root_x + 700
#         win_y = root_y + 100
#         #=======================Dropdown List===========================================================#


#         #=======================Pop Up Initialization==========================================================#
#         self.popUp = Toplevel(self)
#         self.popUp.title("Add Activity")
#         self.popUp.geometry(f'+{win_x}+{win_y}')

#         self.popupFrame = Frame(self.popUp)
#         self.popupFrame.pack(ipadx=50, ipady=50, pady=50)

#         self.labelActivity = Label(self.popupFrame, text="Nama Kegiatan", padx=2, font= self.controller.titlefont, highlightbackground="black", highlightthickness=2)
#         self.labelActivity.grid(row=0, column=0, sticky=W)
#         self.activityBox = Entry(self.popupFrame, textvariable=self.activityName)
#         self.activityBox.grid(row=0, column=1)

#         self.labelCategory = Label(self.popupFrame, text="Kategori     ", padx=2,font= self.controller.titlefont, highlightbackground="black", highlightthickness=2)
#         self.labelCategory.grid(row=1, column=0, sticky=W)
#         self.categoryBox = ttk.Combobox(self.popupFrame, values=["Sport", "Study", "Other"], textvariable=self.categoryName, width=35)
#         self.categoryBox.grid(row=1, column=1)

#         self.labelDeadline = Label(self.popupFrame, text="Batas Waktu  ", padx=2, font= self.controller.titlefont, highlightbackground="black", highlightthickness=2)
#         self.labelDeadline.grid(row=2, column=0, sticky=W)
#         self.deadlineBox = Entry(self.popupFrame, textvariable=self.deadline)
#         self.deadlineBox.grid(row=2, column=1, columnspan=10)

#         self.labelStatus = Label(self.popupFrame, text="Status       ", padx=2, font= self.controller.titlefont, highlightbackground="black", highlightthickness=2)
#         self.labelStatus.grid(row=3, column=0, sticky=W)
#         self.statusBox = ttk.Combobox(self.popupFrame, values=['idle', 'ongoing', 'expired'], textvariable=self.status)
#         self.statusBox.grid(row=3, column=1, columnspan=10)

#         self.submitButton = Button(self.popupFrame, text="Kirim")
#         self.submitButton.grid(row = 6, column = 2, pady = 10)

#         self.cancelButton = Button(self.popupFrame, text="Batal", command=self.popUp.destroy)
#         self.cancelButton.grid(row = 6, column = 3, pady = 10)

#         # ttk.Combobox(self.popupFrame, values=['idle', 'ongoing', 'expired'], textvariable=self.categoryName)

#     def popupCategory():
#         pass


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