from tkinter import *
#หน้าจอทำงานหลัก
def create():
    root = Tk()
    root.title("Registration form by Rujira Navaen")
    root.geometry("350x170")
    root.configure(bg = "#756AB6")
    return root
#ปุ่มข้อความต่างๆ
def widget(root):
    label_title = Label(root, text="Registration Form", font=("Arial", 22),bg='#756AB6',fg="#FFE5E5")
    label_title.grid(row=0, column=0, columnspan=5, padx=10, pady=5,sticky='n')
     # สร้าง Label และ Entry สำหรับกรอก Username
    label_name = Label(root, text="Name:",font=("Arial",16),bg='#756AB6',fg="#FFE5E5")
    label_name.grid(row=1, column=0, padx=90, sticky="w")

    entry_name = Entry(root,highlightbackground='#E0AED0',bg='#FFE5E5')
    entry_name.grid(row=1, column=2, padx=10, pady=5, sticky="w")

    # สร้าง Label และ Entry สำหรับกรอก Email
    label_gmail = Label(root, text="Email:",font=("Arial",16),bg='#756AB6',fg="#FFE5E5")
    label_gmail.grid(row=2, column=0, padx=90, pady=2, sticky="w")

    entry_email = Entry(root,highlightbackground='#E0AED0',bg='#FFE5E5')  
    entry_email.grid(row=2, column=2, padx=10,pady=5, sticky="w")
    
    # สร้าง Label และ Entry สำหรับกรอก Gender
    label_gender = Label(root, text="Gender:",font=("Arial",16),bg='#756AB6',fg="#FFE5E5")
    label_gender.grid(row=3, column=0, padx=90,pady=5, sticky="w")
    #male
    gender_male = Radiobutton(root, text="Male",value=1,bg='#756AB6',fg='#FFE5E5')
    gender_male.grid(row=3, column=2, padx=10,sticky="w")
    #female
    gender_female = Radiobutton(root, text="Female",value=2,bg='#756AB6',fg='#FFE5E5')
    gender_female.grid(row=4, column=2, padx=10,sticky="w")
    #other
    gender_other = Radiobutton(root, text="Other",value=3,bg='#756AB6',fg='#FFE5E5')
    gender_other.grid(row=5, column=2, padx=10,pady=5, sticky="w")

    # สร้าง Label และ Entry สำหรับกรอก phone number
    label_phone_number = Label(root, text="Phone Number:",font=("Arial",16),bg='#756AB6',fg="#FFE5E5")
    label_phone_number.grid(row=6, column=0, padx=90,pady=5, sticky="w")

    entry_phone_number = Entry(root,highlightbackground='#E0AED0',bg='#FFE5E5')  
    entry_phone_number.grid(row=6, column=2, padx=10,pady=5, sticky="w")

    # สร้าง Label และ Entry สำหรับกรอก User Name
    label_usr_name = Label(root, text="User Name:",font=("Arial",16),bg='#756AB6',fg="#FFE5E5")
    label_usr_name.grid(row=7, column=0, padx=90,pady=5, sticky="w")

    entry_usr_name = Entry(root,highlightbackground='#E0AED0',bg='#FFE5E5')  
    entry_usr_name.grid(row=7, column=2, padx=10,pady=5, sticky="w")

    # สร้าง Label และ Entry สำหรับกรอก Pw
    label_pw = Label(root, text="Password:",font=("Arial",16),bg='#756AB6',fg="#FFE5E5")
    label_pw.grid(row=8, column=0, padx=90,pady=5, sticky="w")

    entry_pw = Entry(root,highlightbackground='#E0AED0',bg='#FFE5E5')  
    entry_pw.grid(row=8, column=2, padx=10,pady=5, sticky="w")
    
    # สร้าง Label และ Entry สำหรับกรอก security question
    label_security_question = Label(root, text="Security Question:",font=("Arial",16),bg='#756AB6',fg="#FFE5E5")
    label_security_question.grid(row=9, column=0, padx=90,pady=5, sticky="w")

    entry_security_question = Entry(root,highlightbackground='#E0AED0',bg='#FFE5E5')  
    entry_security_question.grid(row=9, column=2, padx=10,pady=5, sticky="w")
    
    # สร้าง Label และ Entry สำหรับกรอก Answer
    label_answer = Label(root, text="Answer:",font=("Arial",16),bg='#756AB6',fg="#FFE5E5")
    label_answer.grid(row=10, column=0, padx=90,pady=5, sticky="w")

    entry_answer = Entry(root,highlightbackground='#E0AED0',bg='#FFE5E5')  
    entry_answer.grid(row=10, column=2, padx=10,pady=5, sticky="w")
    
    #ปุ่ม🤯
    btn_cancel = Button(root,text='Cancel',highlightbackground='#756AB6',fg='#8ACDD7')
    btn_cancel.grid(row=11, column=1,padx=10, pady=15, sticky="w")
    
    btn_register = Button(root,text='Register',highlightbackground='#756AB6',fg='#FF90BC')
    btn_register.grid(row=11, column=2,padx=10, pady=15, sticky="w")
root=create()
widget(root)
root.mainloop()