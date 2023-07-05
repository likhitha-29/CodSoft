import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
win=tk.Tk()
win.geometry("700x450")
activities=[]
def on_submit():
   activity = '-->'+text.get()
   if activity:
      activities.append(activity)
      label.insert(tk.END, activity)
      text.delete(0, tk.END)
   else:
      messagebox.showwarning("Warning", "Please enter an activity.")
def on_edit():
   index = label.curselection()
   if index:
      index = index[0]
      activity = '-->'+text.get()
      if activity:
         activities[index] = activity
         label.delete(index)
         label.insert(index, activity)
         text.delete(0, tk.END)
      else:
         messagebox.showwarning("Warning", "Please enter an activity.")
   else:
      messagebox.showwarning("Warning", "Please select an activity to edit.")
win.title("To-do-list App")
win.configure(width=500, height=300)
win.configure(bg='lightblue')
str1 = tk.Label(text="Add Items", fg="green",bg="lightblue",font=20)
str1.grid(row=0,column=0)
text=tk.Entry(win,width=33)
text.grid(row=1,column=0)
b=tk.Button(win, text="Submit", command=on_submit,bg="Green")
b.grid(row=1,column=1)
str2 = tk.Label(text="Tasks", fg="green",bg="lightblue")
str2.grid(row=2,column=0)
label=tk.Listbox(win,bg='lightgrey',height=20,width=50)
label.grid(row=3,column=0)
edit_button = tk.Button(win, text="Edit", command=on_edit,bg="blue")
edit_button.grid(row=4,column=0)
delete_button = tk.Button(win, text="Delete", command=lambda listbox=label: listbox.delete(ANCHOR),bg="red")
delete_button.grid(row=5,column=0)
win.mainloop()