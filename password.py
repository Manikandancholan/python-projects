from tkinter import *
from tkinter import messagebox
import mysql.connector as mysql
import bcrypt
from ttkbootstrap import Style
from ttkbootstrap.widgets import Button

def connect():
    try:
        conn = mysql.connect(
            user="root",
            password="Test@123",
            database="rps",
            host="localhost",
            port=3306
        )
        return conn
    except Exception as err:
        print(err)
        raise
        
def login():
    user = username.get()
    passw = password.get()
    connection = connect()
    cursor = connection.cursor()
    
    cursor.execute("SELECT password_hash FROM users WHERE username = %s", (user,))
    result = cursor.fetchone()
    if result:
        stored_hash = result[0].encode('utf-8')
        password_bytes = passw.encode('utf-8')
        if bcrypt.checkpw(password_bytes, stored_hash):
            messagebox.showinfo("Success", "Logged in Successfully!!!")
            app.quit()
        else:
            messagebox.showerror("Error", "Invalid username or password")
            return False
    else:
        print("User not found")
        return False
    
app = Tk()
style = Style(theme="cosmo")
app.geometry("800x500")

username = StringVar()
password = StringVar()

usernameLabel = Label(app, text="Enter Username", font=("Arial", 14))
usernameEntry = Entry(app, textvariable=username, font=("Arial", 12))
passwordLabel = Label(app, text="Enter Password", font=("Arial", 14))
passEntry = Entry(app, textvariable=password, show='*', font=("Arial", 12))

submit = Button(app, text='Login', command=login, bootstyle="primary")

usernameLabel.pack(pady=10)
usernameEntry.pack(pady=10)
passwordLabel.pack(pady=10)
passEntry.pack(pady=10)
submit.pack(pady=20)

app.mainloop()
