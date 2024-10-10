import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta

# Initialize the app window
root = tk.Tk()
root.title("100-Day Countdown")
root.geometry("400x300")
root.configure(bg="#f0f0f0")


total_days = 100


today = datetime.now().date()


start_date = today

def get_current_day(start_date):
 
    days_passed = (today - start_date).days + 1
    current_day = min(days_passed, total_days)
    return current_day

def update_display():

    current_day = get_current_day(start_date)
    remaining_days = total_days - current_day


    day_label.config(text=f"Today is Day {current_day} of 100.")
    if current_day < total_days:
        remaining_label.config(text=f"{remaining_days} days remaining.")
    else:
        remaining_label.config(text="Congratulations! You've reached Day 100!")


main_frame = ttk.Frame(root, padding=20)
main_frame.pack(expand=True)


style = ttk.Style()
style.configure('TLabel', font=('Helvetica', 16), background="#f0f0f0")
style.configure('TButton', font=('Helvetica', 12))

title_label = ttk.Label(main_frame, text="100-Day Countdown", font=("Helvetica", 18, "bold"), anchor="center")
title_label.pack(pady=20)

day_label = ttk.Label(main_frame, text="", anchor="center")
day_label.pack(pady=10)

remaining_label = ttk.Label(main_frame, text="", anchor="center")
remaining_label.pack(pady=10)


refresh_button = ttk.Button(main_frame, text="Refresh", command=update_display)
refresh_button.pack(pady=20)

update_display()


root.mainloop()
