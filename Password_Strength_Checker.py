# Password Strength Checker
# What: Create a tool that evaluates the 
# strength of a password based on length, use of 
# special characters, numbers, and case sensitivity.
# Why: It helps you understand password security 
# concepts and regex patterns.
# Tools: Python (with re library), 
# HTML/JavaScript (for a web-based version).]
#https://www.rexegg.com/regex-quickstart.php
# import tkinter as tk
# from tkinter import messagebox
import re

password = input("Enter password: ")
import re

if (
    len(password) < 8 or
    re.search(r'\d', password) is None or
    re.search(r'[A-Z]', password) is None or
    re.search(r'[a-z]', password) is None or
    re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is None
):
    if len(password) < 8 or len(password) > 16:
        print("Password must be at least 8 characters long but preferably 16 characters long.")
    if re.search(r'\d', password) is None:
        print("Password must contain at least one number.")
    if re.search(r'[A-Z]', password) is None:
        print("Password must contain at least one uppercase letter.")
    if re.search(r'[a-z]', password) is None:
        print("Password must contain at least one lowercase letter.")
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is None:
        print("Password must contain at least one special character.")
    print("Password is weak.")
else:
    print("Password is strong.")


# def check_password():
#     password = password_entry.get()  # Get the password entered by the user
#     feedback = []
    
#     # Check password rules
#     if len(password) < 8 or len(password) > 16:
#         feedback.append("Password must be at least 8 characters long but preferably 16 characters long.")
#     if re.search(r'\d', password) is None:
#         feedback.append("Password must contain at least one number.")
#     if re.search(r'[A-Z]', password) is None:
#         feedback.append("Password must contain at least one uppercase letter.")
#     if re.search(r'[a-z]', password) is None:
#         feedback.append("Password must contain at least one lowercase letter.")
#     if re.search(r'[!@#$%^&*(),.?\":{}|<>]', password) is None:
#         feedback.append("Password must contain at least one special character.")
    
#     # Display the feedback
#     if feedback:
#         messagebox.showwarning("Weak Password", "\n".join(feedback))
#     else:
#         messagebox.showinfo("Strong Password", "Password is strong!")

# # Create the main application window
# root = tk.Tk()
# root.title("Password Strength Checker")
# root.geometry("400x200")
# root.config(bg="green")  # Set the background color to grey

# # Create and place a label for password input
# password_label = tk.Label(root, text="Enter your password:", font=("Arial", 12), bg="grey", fg="black")
# password_label.pack(pady=10)

# # Create and place an entry widget for password
# password_entry = tk.Entry(
#     root,
#     width=30,
#     show="*",
#     font=("Arial", 12),
#     highlightbackground="white",  # Override default background
#     highlightcolor="white",  # Border highlight color
#     highlightthickness=1,
#     fg="black"
# )
# password_entry.pack(pady=10)

# # Create and place a button to check the password
# check_button = tk.Button(root, text="Submit", command=check_password, font=("Arial", 12), bg="blue", fg="white")
# check_button.pack(pady=10)

# # Run the application
# root.mainloop()