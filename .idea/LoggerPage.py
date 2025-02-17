import tkinter as tk
from tkinter import messagebox
import sqlite3
import bcrypt


conn = sqlite3.connect("users.db")
cursor = conn.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
''')
conn.commit()


def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')


def check_password(stored_password, entered_password):
    return bcrypt.checkpw(entered_password.encode('utf-8'), stored_password.encode('utf-8'))


def register():
    username = entry_username.get()
    password = entry_password.get()

    if username and password:
        try:
            hashed_pw = hash_password(password)
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_pw))
            conn.commit()
            messagebox.showinfo("Success", "Registration successful!")
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Username already exists!")
    else:
        messagebox.showerror("Error", "Please enter a username and password.")

def login():
    username = entry_username.get()
    password = entry_password.get()

    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()

    if result and check_password(result[0], password):
        messagebox.showinfo("Success", "Login successful!")
    else:
        messagebox.showerror("Error", "Invalid username or password.")

def show_users():
    cursor.execute("SELECT username FROM users")
    users = cursor.fetchall()

    if users:
        user_list = "\n".join([user[0] for user in users])
        messagebox.showinfo("Registered Users", f"Users:\n{user_list}")
    else:
        messagebox.showinfo("Registered Users", "No users found!")

root = tk.Tk()
root.title("SQL Login Page")
root.geometry("300x250")

tk.Label(root, text="Username:").pack()
entry_username = tk.Entry(root)
entry_username.pack()

tk.Label(root, text="Password:").pack()
entry_password = tk.Entry(root, show="*")
entry_password.pack()

btn_login = tk.Button(root, text="Login", command=login)
btn_login.pack(pady=5)

btn_register = tk.Button(root, text="Register", command=register)
btn_register.pack()

btn_show_users = tk.Button(root, text="Show Users", command=show_users)
btn_show_users.pack(pady=5)

root.mainloop()
