from distutils.log import debug
import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
from tkinter.ttk import *

import scalperNewEgg

root = tk.Tk()

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3)

#logo
"""""
logo = Image.open('logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1,row=0)
"""""

#instruction
instruction = tk.Label(root, text="ATTENTION ! Si vous entrez vos identifiants, l'achat se fera automatiquement, sans votre autorisation.")
instruction.grid(columnspan=3, column=0, row=1)

#Read url in input field
#urlInputTxt = tk.Label(root, text="URL:")
#urlInputTxt.grid(columnspan=1, column=0, row=0)
#urlInput = tk.Entry (root)
#canvas.create_window(300, 140, window=urlInput)

l1 = Label(root, text = "Paypal Email")
l2 = Label(root, text = "Paypal Password")
l3 = Label(root, text = "URL")
# grid method to arrange labels in respective
# rows and columns as specified
l1.place(relx = 0.3, rely = 0.1, anchor = 'center')
l2.place(relx = 0.3, rely = 0.3, anchor = 'center')
l3.place(relx = 0.3, rely = 0.5, anchor = 'center')
  
# entry widgets, used to take entry from user
e1 = Entry(root)
e2 = Entry(root)
e3 = Entry(root)
# this will arrange entry widgets
e1.place(relx = 0.5, rely = 0.1, anchor = 'center')
e2.place(relx = 0.5, rely = 0.3, anchor = 'center')
e3.place(relx = 0.5, rely = 0.5, anchor = 'center')
  
# checkbutton widget
"""""
c1 = Checkbutton(root, text = "Preserve")
c1.grid(row = 2, column = 0, columnspan = 2)
"""""

def start():
    test = e3.get()
    scalperNewEgg.url = test
    scalperNewEgg.test()
    print(test)

#browse button
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, command=lambda:start(), font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
browse_text.set("Start")
browse_btn.place(relx = 0.5, rely = 0.7, anchor = 'center')


root.mainloop()