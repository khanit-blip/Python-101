from tkinter import *
from tkinter import ttk # theme of tk
from tkinter import messagebox

GUI = Tk() # นี่คือหน้าจอหลักของโปรแกรม

GUI.title('โปรแกรมบันทึกข้อมูล') # นี่คือชื่อโปรแกรม
GUI.geometry('500x400') #นี่คือขนาดโปรแกรม

B1 = ttk.Button(GUI,text='จงแสดงเงินกี่บาท')
B1.pack(ipadx=20,ipady=20)


########################
def Button2():
    text = 'ตอนนี้มีเงินในบัญชีอยู่ 300 บาท'
    messagebox.showinfo('เงินในบัญชี',text)

FB1 = Frame(GUI) # คล้ายกระดาน
FB1.place(x=200,y=300)
B2 = ttk.Button(FB1,text='จงแสดงเงินกี่บาท',command=Button2)
B2.pack(ipadx=20, ipady=20)
########################




GUI.mainloop()
