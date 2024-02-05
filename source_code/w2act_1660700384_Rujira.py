
from tkinter import *

def creat() :
    root = Tk()
    root.title("Replace")
    root.geometry("350x170")
    root.configure(bg = "#69C0C0")
    return root
def widget(root):
    title1_lb = Label(root, text = 'Find what',font = 'Tahoma 10')
    title1_lb.grid(row=0, column=0, padx=10, sticky='w')
    title1_2b = Label(root, text = 'Find what',font = 'Tahoma 10')
    title1_2b.grid(row=1, column=0, padx=10, sticky='w')    
    title1_3b = Label(root, text = 'Find what',font = 'Tahoma 10')
    title1_3b.grid(row=1, column=0, padx=10, sticky='w')

    box1 = Entry(root,bg='#FFFFFF',width=15)
    box1.grid(row=0, column=1, padx=15)
    box2 = Entry(root,bg='#FFFFFF', width=15)
    box2.grid(row=1, column=1,padx=15, pady=10)

    up_rad = Radiobutton(root,text='UP', value =1)
    up_rad.grid(row=2, column=1, padx=15, pady=5, sticky='w')

    down_rad = Radiobutton(root, text='Down', value =0)
    down_rad.grid(row=3, column=1, padx=15, sticky='w')
    btn1 = Button(root,text = 'Find Next',width=10)
    btn1.grid(row=0, column=2)
    btn2 = Button(root,text = 'Replace',width=10)
    btn2.grid(row=1, column=2)
    btn3 = Button(root,text = 'Replace all',width=10)
    btn3.grid(row=2, column=2)
    btn4 = Button(root,text = 'Cancel',width=10)
    btn4.grid(row=3, column=2)

root = creat()
widget(root)
root.mainloop()