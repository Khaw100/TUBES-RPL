from tkinter import *
import tkinter as tk
from tkinter import ttk
from connector import *
from tkinter import font as tkfont
from PIL import Image, ImageTk
from dashboardPage import *
from mainFrame import *
from tkinter import messagebox

class dashboardPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.id = controller.id

        self.popupFont = tkfont.Font(family="Verdana", size = 20, weight = "bold", slant='roman')
        

        #===================================================================================================================================================================#

        self.activityID = IntVar()
        self.activityName = StringVar()
        self.categoryID = IntVar()
        self.deadline = StringVar()
        self.status = StringVar()

        #=========================================================================FRAME=====================================================================================#
        # Central Frame
        self.centralframe = Frame(self, background="white")
        self.centralframe.pack(ipady=700, ipadx=700)

        # Label Title
        self.labelTitle = Label(self.centralframe, text="SIBUKIN", background="white", borderwidth=0, fg="BLACK",font=('times new roman',50,'bold'))
        self.labelTitle.pack(side=TOP, fill=X)

        # Button Frame
        self.buttonFrame = Frame(self.centralframe, background="white")
        self.buttonFrame.pack(anchor="center", pady=40)

        # Table Frame
        self.tableframe = Frame(self.centralframe, background="white", highlightbackground="black", highlightthickness=2)
        self.tableframe.pack(anch='center')

        ## , highlightbackground="black", highlightthickness=2

        #=========================================================================BUTTON==================================================================================#

        self.buttonFilter = Button(self.buttonFrame, text = "Filter", width=23, height =2, padx =2)
        # self.buttonFilter.grid(row=0, column=2)
        self.buttonFilter.pack(side = RIGHT, padx = 15)

        self.buttonTambahKategori = Button(self.buttonFrame, text = "+ Tambah Kategori", command= self.popupCategory,width=23, height =2, padx =2)
        # self.buttonTambahKategori.grid(row=0, column=1)
        self.buttonTambahKategori.pack(side = RIGHT, padx = 15)

        self.buttonTambahKegiatan = Button(self.buttonFrame, text = "+ Tambah Kegiatan", command = self.popupActivity, width=23, height =2, padx =2)
        # self.buttonTambahKegiatan.grid(row=0, column=9)
        self.buttonTambahKegiatan.pack(side = RIGHT, padx = 15)

        #===========================================================================TABLE==================================================================================#
        scroll_y = ttk.Scrollbar(self.tableframe, orient=VERTICAL)
        self.todolistTable = ttk.Treeview(self.tableframe, columns=(1,2,3,4,5), show="headings", height="24", yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill = Y)
        scroll_y = ttk.Scrollbar(command=self.todolistTable.yview)
        self.todolistTable.column(1, minwidth=0, width =0, stretch=NO)
        self.todolistTable.heading(1, text="idKegiatan")
        self.todolistTable.heading(2, text="Activity Name")
        self.todolistTable.heading(3, text="Deadline")
        self.todolistTable.heading(4, text="Status")
        self.todolistTable.heading(5, text="Category Name")

        self.todolistTable['show']='headings'
        self.todolistTable.pack(fill=BOTH, expand=1)
        # self.buttonFrame.place(y=100, width=300, height=50)
        # label = tk.Label(self,text="Dashboard page \n" + controller.id.get(),font= controller.titlefont, highlightbackground="yellow", highlightthickness=2)
        # label.pack()
        # bou = tk.Button(self, text="to next page", command= lambda: controller.up_frame("PageOne"))
        # bou.pack()

        self.fetchTodayData()

    #========================================================================OTHER FUNCTION==========================================================================#
    def fetchTodayData(self):
        self.todolistTable.delete()
        self.dbconnector = connector("localhost", "wipiii", "miscrit10", "rpl")
        self.dbconnector.openConnection()
        todayData = self.dbconnector.allToDoList()
        for row in todayData:
            self.todolistTable.insert('', END, values=row)

    def tambahKegiatan(self):
        try:
            if self.activityName.get() == "" or self.deadline.get() == "":
                messagebox.showerror("Error","All fields are required")
            else:
                self.dbconnector = connector("localhost", "wipiii", "miscrit10", "rpl")
                self.dbconnector.openConnection()
                data = self.dbconnector.allToDoList()
                actID = len(data)+1
                self.dbconnector.addActivity(actID, self.activityName.get(), self.status.get(), self.deadline.get(), self.categoryID.get())
        except:
            messagebox.showerror("Error", "Error Occured")
        self.activityName.set("")
        self.categoryID.set("")
        self.status.set("")
        self.deadline.set("")
        self.todolistTable.destroy()

    def tambahKategori(self):
        try:
            if self.activityName.get() == "" or self.deadline.get() == "":
                messagebox.showerror("Error","All fields are required")
            else:
                self.dbconnector = connector("localhost", "wipiii", "miscrit10", "rpl")
                self.dbconnector.openConnection()
                data = self.dbconnector.allToDoList()
                actID = len(data)+1
                self.dbconnector.addActivity(actID, self.activityName.get(), self.status.get(), self.deadline.get(), self.categoryID.get())
        except:
            messagebox.showerror("Error", "Error Occured")
        pass

    def clearEntry(self):
        self.activityName.set("")
        self.categoryID.set("")
        self.status.set("")
        self.deadline.set("")



    def popupActivity(self):

        #========================Make The Pop Up Windows Position At The Center=================================#
        # Get main window position
        root_x = self.winfo_rootx()
        root_y = self.winfo_rooty()

        # Add Offset
        win_x = root_x + 700
        win_y = root_y + 100

        #=======================Pop Up Initialization==========================================================#
        self.popUp = Toplevel(self)
        self.popUp.title("Add Activity")
        self.popUp.geometry(f'+{win_x}+{win_y}')

        self.popupFrame = Frame(self.popUp, highlightbackground="black", highlightthickness=2)
        self.popupFrame.pack(ipadx=50, ipady=50, pady=50)


        self.labelActivity = Label(self.popupFrame, text="Nama Kegiatan", padx=2, font= self.controller.titlefont, highlightbackground="black", highlightthickness=2)
        self.labelActivity.grid(row=0, column=0, sticky=W)
        self.activityBox = Entry(self.popupFrame, textvariable=self.activityName)
        self.activityBox.grid(row=0, column=1)

        self.labelCategory = Label(self.popupFrame, text="Kategori     ", padx=2,font= self.controller.titlefont, highlightbackground="black", highlightthickness=2)
        self.labelCategory.grid(row=1, column=0, sticky=W)
        self.categoryBox = ttk.Combobox(self.popupFrame, values=[1,2,3,4], textvariable=self.categoryID, width=35)
        self.categoryBox.grid(row=1, column=1)

        self.labelDeadline = Label(self.popupFrame, text="Batas Waktu  ", padx=2, font= self.controller.titlefont, highlightbackground="black", highlightthickness=2)
        self.labelDeadline.grid(row=2, column=0, sticky=W)
        self.deadlineBox = Entry(self.popupFrame, textvariable=self.deadline)
        self.deadlineBox.grid(row=2, column=1)

        self.labelStatus = Label(self.popupFrame, text="Status       ", padx=2, font= self.controller.titlefont, highlightbackground="black", highlightthickness=2)
        self.labelStatus.grid(row=3, column=0, sticky=W)
        self.statusBox = ttk.Combobox(self.popupFrame, values=['idle', 'ongoing', 'expired'], textvariable=self.status)
        self.statusBox.grid(row=3, column=0)

        self.submitButton = Button(self.popupFrame, text="Kirim", command = self.tambahKegiatan)
        self.submitButton.grid(row = 6, column = 0, pady = 1, sticky = W)

        self.cancelButton = Button(self.popupFrame, text="Batal", command=self.popUp.destroy)
        self.cancelButton.grid(row = 6, column = 3, pady = 10)

    def popupCategory(self):
        #========================Make The Pop Up Windows Position At The Center=================================#
        # Get main window position
        root_x = self.winfo_rootx()
        root_y = self.winfo_rooty()

        # Add Offset
        win_x = root_x + 700
        win_y = root_y + 100

        #=======================Pop Up Initialization==========================================================#
        self.popUp = Toplevel(self)
        self.popUp.title("Add Category")
        self.popUp.geometry(f'+{win_x}+{win_y}')
        self.popUp.resizable(0,0)

        self.popUp.columnconfigure(0, weight=1)
        self.popUp.columnconfigure(1, weight=3)


        self.popupFrame = Frame(self.popUp, highlightbackground="black", highlightthickness=2)
        self.popupFrame.pack(ipadx=50, ipady=50, pady=50)
        #========================widget================#
        self.labelTitle = Label(self.popupFrame, text = "Tambah Kategori", font=self.popupFont, highlightbackground="black", highlightthickness=2)
        self.labelKategori= Label(self.popupFrame, text="Nama Kategori", font= self.controller.titlefont, highlightbackground="black", highlightthickness=2, padx=5)
        self.categoryBox = Entry(self.popupFrame, textvariable=self.categoryID, width= 30)
        self.submitButton = Button(self.popupFrame, text="Kirim")
        #===========POSITIONING=====================#
        # self.labelTitle.grid(row = 0, column = 1)
        self.labelTitle.pack(side=TOP, anchor=CENTER)
        # self.labelKategori.grid(row = 3, column = 0, sticky = E, padx = 5)
        self.labelKategori.pack(side=LEFT)
        # self.categoryBox.grid(row=3, column = 1, sticky = W, padx=5)
        self.categoryBox.pack(side=LEFT, expand=True)
        self.submitButton.pack(side=BOTTOM, anchor=CENTER, fill=X, expand=True)

    def popUpFilter(self):
        #========================Make The Pop Up Windows Position At The Center=================================#
        # Get main window position
        root_x = self.winfo_rootx()
        root_y = self.winfo_rooty()

        # Add Offset
        win_x = root_x + 700
        win_y = root_y + 100

        #=======================Pop Up Initialization==========================================================#
        self.popUp = Toplevel(self)
        self.popUp.title("Add Category")
        self.popUp.geometry(f'+{win_x}+{win_y}')
        self.popUp.resizable(0,0)

        self.popUp.columnconfigure(0, weight=1)
        self.popUp.columnconfigure(1, weight=3)

        #======================================================================================================#

        self.pFrame = Frame(self.popUp, highlightbackground="black", highlightthickness=2)
        self.pFrame.pack(ipadx=50, ipady=50, pady=50)

        self.p1Frame = Frame(self.popUp, bg="blue")
        self.p1Frame.pack(side = LEFT)

        self.p2Frame = Frame(self.popUp, bg="red")
        self.p2Frame.pack(side=RIGHT)




