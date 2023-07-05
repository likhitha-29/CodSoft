import tkinter as tk
from tkinter import *
import string, random
from tkinter import messagebox
win=tk.Tk()
win.geometry("700x450")
password = StringVar()
combinations = [string.punctuation, string.ascii_uppercase, string.digits, string.ascii_lowercase] 
def on_generate():
    password1 = ""
    t=int(text1.get())
    for y in range(t):
        ch = random.choice(combinations)   
        password1 = password1 + random.choice(ch) 
    text2.delete(0,END)
    text2.insert('1',password1)
def on_accept():
          messagebox.showwarning("Accepted", "Your selected Password is accepted.",icon='info')
          on_reset()
def on_reset():
    text.delete(0,END)
    text1.delete(0,END)
    text2.delete(0,END)
win.title("Password Generator")
win.configure(width=500, height=300)
win.configure(bg='white')
str1 = tk.Label(text="Password Generator", fg="green",bg="white",font=20)
str1.grid(row=0,column=1)
str2 = tk.Label(text="Enter username: ", fg="black",bg="white")
str2.grid(row=2,column=0)
text=tk.Entry(win,width=33)
text.grid(row=2,column=1)
str3 = tk.Label(text="Enter password length: ", fg="black",bg="white")
str3.grid(row=3,column=0)
text1=tk.Entry(win,width=33)
text1.grid(row=3,column=1)
str4 = tk.Label(text="Generated Password: ", fg="black",bg="white")
str4.grid(row=4,column=0)
text2=tk.Entry(win,width=33)
text2.grid(row=4,column=1)
generate_button = tk.Button(win, text="Generate Password", command=on_generate,bg="blue")
generate_button.grid(row=5,column=1)
accept_button = tk.Button(win, text="Accept",command=on_accept,bg="white")
accept_button.grid(row=6,column=1)
reset_button = tk.Button(win, text="Reset", command=on_reset,bg="white")
reset_button.grid(row=7,column=1)
win.mainloop()