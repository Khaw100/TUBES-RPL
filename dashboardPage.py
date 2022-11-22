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
        self.categoryName = StringVar()
        self.deadline = StringVar()
        self.status = StringVar()


        self.listCategory = [] 

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

        #=========================================================================BUTTON==================================================================================#
        
        self.buttonDelete = Button(self.buttonFrame, text= "Delete", width=23, height =2, padx =2)
        self.buttonDelete.pack(side = RIGHT, padx = 15)

        self.buttonFilter = Button(self.buttonFrame, text = "Filter", command= self.popUpFilter, width=23, height =2, padx =2)
        self.buttonFilter.pack(side = RIGHT, padx = 15)

        self.buttonTambahKategori = Button(self.buttonFrame, text = "+ Tambah Kategori", command= self.popupCategory,width=23, height =2, padx =2)
        self.buttonTambahKategori.pack(side = RIGHT, padx = 15)

        self.buttonTambahKegiatan = Button(self.buttonFrame, text = "+ Tambah Kegiatan", command = self.popupActivity, width=23, height =2, padx =2)
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
        self.dbconnector = connector("localhost", "root", "password", "rpl")
        self.dbconnector.openConnection()
        todayData = self.dbconnector.allToDoList()
        for row in todayData:
            self.todolistTable.insert('', END, values=row)

    def tambahKegiatan(self):
        try:
            if self.activityName.get() == "":
                messagebox.showerror("Error","All fields are required")
            else:
                self.dbconnector = connector("localhost", "root", "password", "rpl")
                self.dbconnector.openConnection()
                data = self.dbconnector.allToDoList()
                actID = len(data)+1
                for i in range(len(self.listCategory)):
                    if self.categoryName == self.listCategory[i][1]:
                        self.categoryID = self.listCategory[i][0]
                self.dbconnector.addActivity(actID, self.activityName.get(), self.status.get(), self.deadline.get(), self.categoryID.get())
        except:
            messagebox.showerror("Error", "Error Occured")
        self.activityName.set("")
        self.categoryID.set("")
        self.status.set("")
        self.deadline.set("")
        self.popUp.destroy()

    def tambahKategori(self):
        try:
            if self.categoryName.get() == "" :
                messagebox.showerror("Error","All fields are required")
            else:
                self.dbconnector = connector("localhost", "root", "password", "rpl")
                self.dbconnector.openConnection()
                data = self.dbconnector.allCategory()
                catID = len(data)+1
                self.dbconnector.addCategory(catID, self.categoryName.get())
        except:
            messagebox.showerror("Error", "Error Occured")
        self.listCategory.append(self.categoryName.get())
        print(self.listCategory)
        self.categoryName.set("")
        self.popUp.destroy()

    def filterToDoList(self):
        try:
            if self.status.get() != "" and self.categoryName.get() == "":
                self.dbconnector = connector("localhost", "root", "password", "rpl")
                self.dbconnector.openConnection()
                data = self.dbconnector.filterStatus()
                for row in data:
                    self.todolistTable.insert('', END, values=row)
            elif self.status.get() == "" and self.categoryName.get() != "":
                self.dbconnector = connector("localhost", "root", "password", "rpl")
                self.dbconnector.openConnection()
                data = self.dbconnector.filterKategori()
                for row in data:
                    self.todolistTable.insert('', END, values=row)
        except:
            messagebox.showerror("Error", "Error Occured")

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
        #+##+#+#+#+

        self.labelTitle = Label(self.popupFrame, text = "Tambah Kegiatan", font=self.popupFont)
        self.labelSpacing = Label(self.popupFrame)
        self.labelSpacing1 = Label(self.popupFrame)

        # Activity
        self.labelActivity= Label(self.popupFrame, text="Nama Kegiatan", font= self.controller.titlefont, padx=5)
        self.activityBox = Entry(self.popupFrame, textvariable=self.activityName, width= 30)
        self.labelSpacing2 = Label(self.popupFrame)

        # Category
        self.labelCategory= Label(self.popupFrame, text="Kategori", font= self.controller.titlefont, padx=5)
        self.categoryBox = ttk.Combobox(self.popupFrame, values=['Olahraga'], textvariable=self.categoryName, width = 30)
        self.labelSpacing3 = Label(self.popupFrame)

        # Deadline
        self.labelDeadline= Label(self.popupFrame, text="Batas Waktu (YYYY-MM-DD)", font= self.controller.titlefont, padx=5)
        self.deadlineBox = Entry(self.popupFrame, textvariable=self.deadline, width= 30)
        self.labelSpacing4 = Label(self.popupFrame)


        # Status
        self.labelStatus= Label(self.popupFrame, text="Status", font= self.controller.titlefont, padx=5)
        self.statusBox = ttk.Combobox(self.popupFrame, values=['idle', 'ongoing', 'expired'], textvariable=self.status, width = 30)
        self.labelSpacing5 = Label(self.popupFrame)

        # Button
        self.submitButton = Button(self.popupFrame, text="Kirim", command=self.tambahKegiatan)
        
        # #===========POSITIONING=====================#
        self.labelTitle.pack(side=TOP, anchor=CENTER)
        self.labelSpacing.pack(side =TOP)
        self.labelSpacing1.pack(side =TOP)

        # Activity
        self.labelActivity.pack(side=TOP)
        self.activityBox.pack(side=TOP, expand=True)
        self.labelSpacing2.pack(side =TOP)

        # Category
        self.labelCategory.pack(side=TOP)
        self.categoryBox.pack(side=TOP, expand=True)
        self.labelSpacing3.pack(side =TOP)

        # Deadline
        self.labelDeadline.pack(side=TOP)
        self.deadlineBox.pack(side=TOP, expand=True)
        self.labelSpacing4.pack(side =TOP)

        # Status
        self.labelStatus.pack(side=TOP)
        self.statusBox.pack(side=TOP, expand=True)
        self.labelSpacing5.pack(side =TOP)

        # Button
        self.submitButton.pack(side=TOP, expand=True)

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
        #========================FRAME==========================================================================#
        self.popupFrame = Frame(self.popUp, highlightbackground="black", highlightthickness=2)
        self.popupFrame.pack(ipadx=50, ipady=50, pady=50)
        #========================widget================#
        self.labelTitle = Label(self.popupFrame, text = "Tambah Kategori", font=self.popupFont)
        self.labelSpacing = Label(self.popupFrame)
        self.labelSpacing1 = Label(self.popupFrame)
        self.labelKategori= Label(self.popupFrame, text="Nama Kategori", font= self.controller.titlefont)
        self.labelSpacing2 = Label(self.popupFrame)
        self.categoryBox = Entry(self.popupFrame, textvariable=self.categoryName, width= 30)
        self.labelSpacing3 = Label(self.popupFrame)
        self.submitButton = Button(self.popupFrame, text="Kirim", command=self.tambahKategori)
        #===========POSITIONING=====================#
        self.labelTitle.pack(side=TOP, anchor=CENTER)
        self.labelSpacing.pack(side =TOP)
        self.labelSpacing1.pack(side =TOP)
        self.labelKategori.pack(side=TOP)
        self.labelSpacing2.pack(side =TOP)
        self.categoryBox.pack(side=TOP)
        self.labelSpacing3.pack(side =TOP)
        self.submitButton.pack(side=TOP)

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
        self.popUp.title("Filter")
        self.popUp.geometry(f'+{win_x}+{win_y}')
        self.popUp.resizable(0,0)
        #===========================FRAME=========================================================#

        self.popupFrame = Frame(self.popUp, highlightbackground="black", highlightthickness=2)
        self.popupFrame.pack(ipadx=50, ipady=50, pady=50)
        #========================widget================#
        self.labelTitle = Label(self.popupFrame, text = "Filter", font=self.popupFont)
        self.labelSpacing = Label(self.popupFrame)
        self.labelSpacing1 = Label(self.popupFrame)
        self.labelStatus= Label(self.popupFrame, text="Status", font= self.controller.titlefont, padx=5)
        self.statusBox = ttk.Combobox(self.popupFrame, values=['idle', 'ongoing', 'expired'], textvariable=self.status, width = 30)
        self.labelSpacing2 = Label(self.popupFrame)
        self.labelKategori= Label(self.popupFrame, text="Kategori", font= self.controller.titlefont, padx=5)
        self.kategoriBox = ttk.Combobox(self.popupFrame, values=self.listCategory, textvariable=self.categoryName, width = 30)
        self.labelSpacing3 = Label(self.popupFrame)
        self.submitButton = Button(self.popupFrame, text="Kirim", command=self.filterToDoList)
        
        #===========POSITIONING=====================#
        self.labelTitle.pack(side=TOP, anchor=CENTER)
        self.labelSpacing.pack(side =TOP)
        self.labelSpacing1.pack(side =TOP)
        self.labelStatus.pack(side=TOP)
        self.statusBox.pack(side=TOP, expand=True)
        self.labelSpacing2.pack(side =TOP)
        self.labelKategori.pack(side=TOP)
        self.kategoriBox.pack(side=TOP, expand=True)
        self.labelSpacing3.pack(side =TOP)
        self.submitButton.pack(side=TOP, expand=True)




