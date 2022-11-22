from tkinter import *
import tkinter as tk
from tkinter import ttk
from connector import *

# class defaultpage():
#     def __init__(self) -> None:
#         pass

# Constructor Function
root= Tk()
root.title("SIBUKIN")
root.geometry("800x800+400+100")
root.resizable(False, False)

mycn = connector("localhost", "wipiii", "miscrit10", "rpl")
mycn.openConnection()
data = mycn.allToDoList()
total = mycn._session.rowcount
print(f"Total Data Entries: {total}")

backgroundFrame = tk.Frame(root, bg='grey')
backgroundFrame.pack_propagate(0)
backgroundFrame.pack(fill='both', side='left', expand='True')

frameTable = Frame(backgroundFrame)
frameTable.pack(side=tk.LEFT, padx=20)



# greenFrame = tk.Frame(backgroundFrame, width=100, height=100, bg='green')
# greenFrame.pack_propagate(0)
# greenFrame.pack(side='top', padx=0, pady=0)

table = ttk.Treeview(frameTable, columns=(1,2,3,4,5), show="headings", height="6")
table.pack()

table.column(1, minwidth=0, width =0, stretch=NO)
table.heading(1, text="idKegiatan")
table.heading(2, text="Activity Name")
table.heading(3, text="Category Name")
table.heading(4, text="Deadline")
table.column(4, width=100)
table.heading(5, text="Status")
table.column(5, width=100)

# ICON
image_icon = PhotoImage(file="image/list.png")
root.iconphoto(False, image_icon)

print('aaaaaaaaaaaaaaaaaa')
print(data)
print(data[0][1])
print(type(data))
for i in range(len(data)):
    table.insert('','end',values=data[i])




root.mainloop()