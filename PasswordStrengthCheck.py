import tkinter as tk
from tkinter import messagebox
import re

def check_password_strength():
    password = entry.get()

    # Criteria for password strength
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[ !@#$%^&*()_+{}\[\]:;<>,.?/~\-]", password) is None

    # Calculate strength
    errors = [length_error, digit_error, uppercase_error, lowercase_error, symbol_error]
    score = 5 - sum(errors)

    if length_error:
        strength = "Too Short"
        color = "red"
    elif score == 5:
        strength = "Very Strong"
        color = "green"
    elif score >= 4:
        strength = "Strong"
        color = "blue"
    elif score >= 3:
        strength = "Medium"
        color = "orange"
    else:
        strength = "Weak"
        color = "red"

    result_label.config(text=f"Password Strength: {strength}", fg=color)

    # Optional: show which criteria are missing
    criteria = []
    if length_error: criteria.append("at least 8 characters")
    if uppercase_error: criteria.append("uppercase letter")
    if lowercase_error: criteria.append("lowercase letter")
    if digit_error: criteria.append("digit")
    if symbol_error: criteria.append("special symbol")

    if criteria:
        tips = "Include: " + ", ".join(criteria)
    else:
        tips = "Great password!"

    tips_label.config(text=tips)

# Setup GUI
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x200")
root.resizable(False, False)

label = tk.Label(root, text="Enter your password:")
label.pack(pady=10)

entry = tk.Entry(root, width=30, show="*")
entry.pack()

check_btn = tk.Button(root, text="Check Strength", command=check_password_strength)
check_btn.pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 14))
result_label.pack()

tips_label = tk.Label(root, text="", font=("Helvetica", 10))
tips_label.pack(pady=5)

root.mainloop()
