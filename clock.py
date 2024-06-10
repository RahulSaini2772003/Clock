import tkinter as tk
from tkinter import messagebox
import time 
alarms = []
current_alarm_index = 0
def update_time():
        current_time = time.strftime('%H:%M:%S %p')
        cl.config(text=current_time)
        check_alarms()
        root.after(1000, update_time)
        
def check_alarms():
    current_time = time.strftime('%H:%M')
    for alarm in alarms:
        if alarm == current_time:
            messagebox.showinfo("Alarm", "Time to wake up!")
            
def add_alarm():
        new_alarm = tk.simpledialog.askstring("Add Alarm", "Enter alarm time (HH:MM):")
        if new_alarm:
            alarms.append(new_alarm)

def remove_alarm():
        if alarms:
            alarms.pop(0)
root = tk.Tk() 
root.title("Basic Clock")
root.geometry("400x500")
root.iconphoto(True,tk.PhotoImage(file='img\logo.png'))
frm = tk.Label(root,text="My Alarm Clock", font=('Arial', 24),pady=40,padx=10,width=20,bg='pink')
frm.grid(row=0,column=0)
cl = tk.Label(root, font=('Arial', 24),pady=40,width=20,bg='pink')
cl.place(x=7,y=130)
frm = tk.Button(root,text="Add Alarm", font=('Arial', 24),pady=40,padx=10,width=20,bg='pink',command=add_alarm)
frm.place(x=0,y=260)
frm = tk.Button(root,text="Remove Alarm", font=('Arial', 24),pady=40,padx=10,width=20,bg='pink',command=remove_alarm)
frm.place(x=0,y=380)

update_time()
root.mainloop()




