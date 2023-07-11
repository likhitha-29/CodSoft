import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
win=tk.Tk()
win.geometry("450x450")
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
def on_done():
   index=label.curselection()
   if index:
      temp=index[0]
      temp_marked=label.get(index)
      temp_marked=temp_marked+" ✔"
      label.delete(temp)
      label.insert(temp,temp_marked)
   else:
      messagebox.showwarning("Warning", "Please select an activity to edit.")
win.title("To-do-list App")
win.configure(width=500, height=300)
win.configure(bg='lightblue')
left_frame  =  Frame(win,  width=250,  height=500,  bg='#ffb6c1')
left_frame.place(x=10,  y=10,  relx=0.01,  rely=0.01)
right_frame  =  Frame(win,  width=600,  height=500,  bg='#368BC1')
right_frame.place(x=270,  y=10,  relx=0.01,  rely=0.01)
str1 = tk.Label(left_frame,text="Add Items", fg="green",bg="#ffb6c1",font=20)
str1.place(relx=0.3,  rely=0.05)
text=tk.Entry(left_frame,width=50)
text.place(rely=0.15)
b=tk.Button(left_frame, text="Submit", command=on_submit,bg="Green")
b.place(relx=0.4,  rely=0.20)
str2 = tk.Label(right_frame,text="Tasks", fg="green",bg="lightblue")
str2.place(relx=1.0,  rely=0.05)
label=tk.Listbox(right_frame,bg='lightgrey',height=20,width=100)
label.place(y=10,  relwidth=1,  relheight=1)
edit_button = tk.Button(left_frame, text="Edit", command=on_edit,bg="#FED8B1")
edit_button.place(relx=0.1,  rely=0.35)
mark_button = tk.Button(left_frame, text="Mark as Done", command=on_done,bg="orange")
mark_button.place(relx=0.1,  rely=0.45)
delete_button = tk.Button(left_frame, text="Delete", command=lambda listbox=label: listbox.delete(ANCHOR),bg="#FF5733")
delete_button.place(relx=0.1,  rely=0.55)
win.mainloop()
