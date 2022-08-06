

from tkinter import *
import webbrowser as wb

def open_url():
    text = str(e.get())
    wb.open(text)

root = Tk()

root.title("Squad Students ")
root.geometry("400x500")

l = Label(root,text="Url :")
l.place (x = 10 , y = 20)

# 
e = Entry(root,width = 30)
e.place(x = 50 , y = 20)

#
b = Button(root,text = "Brows" , command = open_url)
b.place(x = 40 , y = 40)

root.mainloop()























