from tkinter import *



window = Tk()
root=Tk()
window.title('Hello Python')
window.geometry("600x400")



lbl1 = Label(window, text="First Number")
lbl2 = Label(window, text="Second Number")
lbl3 = Label(window, text="Result")


t1 = Entry()
t2 = Entry()
t3 = Entry()


lbl1.place(x=100, y=50)
t1.place(x=200, y=50)
lbl2.place(x=90, y=100)
t2.place(x=200, y=100)



def add():
    num1 = int(t1.get())
    num2 = int(t2.get())
    result = num1 + num2
    t3.delete(0, END)
    t3.insert(END, str(result))



def sub():
    num1 = int(t1.get())
    num2 = int(t2.get())
    result = num1 - num2
    t3.delete(0, END)
    t3.insert(END, str(result))



def clear():
    t1.delete(0, END)
    t2.delete(0, END)
    t3.delete(0, END)



b1 = Button(window, text='Add', command=add)
b2 = Button(window, text='Subtract', command=sub)
b3 = Button(window, text='Clear Result', command=clear)


b1.place(x=100, y=150)
b2.place(x=200, y=150)
b3.place(x=200, y=250)
lbl3.place(x=100, y=200)
t3.place(x=200, y=200)

window.mainloop()
