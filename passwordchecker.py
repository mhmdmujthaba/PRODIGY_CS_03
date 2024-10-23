import re
import tkinter as tk
from tkinter import messagebox, font

def password_strength_checker(password):
    length_check = len(password) >= 8
    upper_check = re.search(r'[A-Z]', password) is not None
    lower_check = re.search(r'[a-z]', password) is not None
    digit_check = re.search(r'\d', password) is not None
    special_check = re.search(r'[@$!%*?&]', password) is not None

    score = sum([length_check, upper_check, lower_check, digit_check, special_check])
    
    if score < 3:
        strength = "Weak"
    elif score == 3:
        strength = "Moderate"
    else:
        strength = "Strong"

    feedback = []
    if not length_check:
        feedback.append("Password should be at least 8 characters long.")
    if not upper_check:
        feedback.append("Password should contain at least one uppercase letter.")
    if not lower_check:
        feedback.append("Password should contain at least one lowercase letter.")
    if not digit_check:
        feedback.append("Password should contain at least one digit.")
    if not special_check:
        feedback.append("Password should contain at least one special character (e.g., @$!%*?&).")
    
    return strength, feedback

def check_password():
    password = entry.get()
    strength, feedback = password_strength_checker(password)
    
    result_message = f"Password Strength: {strength}\n"
    if feedback:
        result_message += "Feedback:\n" + "\n".join(f"- {message}" for message in feedback)
    
    messagebox.showinfo("Password Strength Result", result_message)

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x300")
root.configure(bg="#000000")  

header_font = font.Font(family="Helvetica", size=16, weight="bold")
label_font = font.Font(family="Helvetica", size=12)
button_font = font.Font(family="Helvetica", size=10, weight="bold")

header = tk.Label(root, text="Check Your Password Strength", bg="#000000", fg="#F7E1A0", font=header_font)
header.pack(pady=20)

frame = tk.Frame(root, bg="#000000")
frame.pack(pady=10)

label = tk.Label(frame, text="Enter your password:", bg="#000000", fg="#FFFFFF", font=label_font)
label.pack(pady=5)

entry = tk.Entry(frame, show="*", width=30, font=label_font, bg="#FFFFFF", fg="#000000")
entry.pack(pady=5)

def on_enter(e):
    check_button['background'] = '#DDDDDD'  
def on_leave(e):
    check_button['background'] = '#FFFFFF'  

check_button = tk.Button(root, text="Check Strength", command=check_password, font=button_font, 
                         bg="#FFFFFF", fg="#000000", activebackground="#DDDDDD", activeforeground="#000000", padx=20, pady=5)
check_button.pack(pady=20)

check_button.bind("<Enter>", on_enter)
check_button.bind("<Leave>", on_leave)

root.mainloop()
