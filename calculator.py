import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
win=tk.Tk()
win.geometry("200x150")
win.title("Calculator")
win.configure(bg='white')
equation=""
def fun(n):
    global equation
    equation=equation+str(n)
    eqn.set(equation)
def result():
    try:
        global equation
        res = str(eval(equation))
        eqn.set(res)
        equation = ""
    except:
        eqn.set(" error ")
        equation = ""
def clear():
    global equation
    eqaution=""
    eqn.set("")
def dele():
    global equation
    equation=equation[:len(equation)-1]
    eqn.set(equation)
eqn=StringVar()
text=tk.Entry(win,width=33,textvariable = eqn,highlightthickness=1)
text.config(highlightbackground = "black", highlightcolor= "black")
text.grid(row=0,columnspan=4)
btn_c = Button(win, text=' c ', fg='white', bg='red',command=clear, height=1, width=5)
btn_c.grid(row=2, column=0)
btn_7 = Button(win, text=' <-- ', fg='white', bg='grey',command=lambda: dele(), height=1, width=5)
btn_7.grid(row=2, column=1)
btn_8 = Button(win, text=' ^ ', fg='white', bg='grey',command=lambda: fun('**'), height=1, width=5)
btn_8.grid(row=2, column=2)
btn_6 = Button(win, text=' / ', fg='white', bg='grey',command=lambda: fun('/'), height=1, width=5)
btn_6.grid(row=2, column=3)
btn1 = Button(win, text=' 1 ', fg='white', bg='black',command=lambda: fun(1), height=1, width=5)
btn1.grid(row=3, column=0)
btn2 = Button(win, text=' 2 ', fg='white', bg='black',command=lambda: fun(2), height=1, width=5)
btn2.grid(row=3, column=1)
btn3 = Button(win, text=' 3 ', fg='white', bg='black',command=lambda: fun(3), height=1, width=5)
btn3.grid(row=3, column=2)
btn_3 = Button(win, text=' * ', fg='white', bg='grey',command=lambda: fun('*'), height=1, width=5)
btn_3.grid(row=3, column=3)
btn4 = Button(win, text=' 4 ', fg='white', bg='black',command=lambda: fun(4), height=1, width=5)
btn4.grid(row=4, column=0)
btn5 = Button(win, text=' 5 ', fg='white', bg='black',command=lambda: fun(5), height=1, width=5)
btn5.grid(row=4, column=1)
btn6 = Button(win, text=' 6 ', fg='white', bg='black',command=lambda: fun(6), height=1, width=5)
btn6.grid(row=4, column=2)
btn_3 = Button(win, text=' - ', fg='white', bg='grey',command=lambda: fun('-'), height=1, width=5)
btn_3.grid(row=4, column=3)
btn7 = Button(win, text=' 7 ', fg='white', bg='black',command=lambda: fun(7), height=1, width=5)
btn7.grid(row=5, column=0)
btn8 = Button(win, text=' 8 ', fg='white', bg='black',command=lambda: fun(8), height=1, width=5)
btn8.grid(row=5, column=1)
btn9 = Button(win, text=' 9 ', fg='white', bg='black',command=lambda: fun(9), height=1, width=5)
btn9.grid(row=5, column=2)
btn_4 = Button(win, text=' + ', fg='white', bg='grey',command=lambda: fun('+'), height=1, width=5)
btn_4.grid(row=5, column=3)
btn_1 = Button(win, text=' % ', fg='white', bg='black',command=lambda: fun('%'), height=1, width=5)
btn_1.grid(row=6, column=0)
btn0 = Button(win, text=' 0 ', fg='white', bg='black',command=lambda: fun(0), height=1, width=5)
btn0.grid(row=6, column=1)
btn_2 = Button(win, text=' . ', fg='white', bg='black',command=lambda: fun('.'), height=1, width=5)
btn_2.grid(row=6, column=2)
btn_5 = Button(win, text=' = ', fg='white', bg='grey',command=result, height=1, width=5)
btn_5.grid(row=6, column=3)
win.mainloop()