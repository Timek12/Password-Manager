from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import re

login_window = Tk()

login_window.geometry('1000x600')
login_window.title('Registration Form')
login_window.configure(bg="#fff")
login_window.resizable(False, False)


def hide_input():
    global open_eye, close_eye
    open_eye = Image.open('close_eye.png')
    open_eye = open_eye.resize((30, 30), Image.ANTIALIAS)
    open_eye = ImageTk.PhotoImage(open_eye)
    eye_button.config(image=open_eye)
    password_entry.config(show='*')

    eye_button.config(command=show_input)


def show_input():
    global open_eye, close_eye
    close_eye = Image.open('open_eye.png')
    close_eye = close_eye.resize((35, 35), Image.ANTIALIAS)
    close_eye = ImageTk.PhotoImage(close_eye)
    eye_button.config(image=close_eye)
    password_entry.config(show='')

    eye_button.config(command=hide_input)


def validate_email(self, email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))


def sign_in():
    email = email_entry.get()
    password = password_entry.get()
    if email == 'admin@gmail.com' and password == 'admin123':
        screen = Toplevel(login_window)
        screen.title('App')
        screen.geometry('1000x600')
        screen.config(bg='white')

        Label(screen, text='Hello Admin!', bg='#fff', font=('Calibri(Body)', 50, 'bold')).pack(expand=True)

        screen.mainloop()
    else:
        messagebox.showerror('Incorrect input data', 'Invalid email or password')


image_open = Image.open("img4.jpg")
image_open = image_open.resize((500, 500))
img = ImageTk.PhotoImage(image_open)

Label(login_window, image=img, bg='white').place(x=50, y=50, height=500, width=550)

frame = Frame(login_window, width=350, height=350, bg="white")
frame.place(x=570, y=100)

heading = Label(frame, text='Sign in', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=110, y=5)


def email_enter(event):
    email_entry.delete(0, 'end')


def email_leave(event):
    name = email_entry.get()
    if name == '':
        email_entry.insert(0, 'e-mail')


email_entry = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
email_entry.place(x=30, y=80)
email_entry.insert(0, 'e-mail')
email_entry.bind('<FocusIn>', email_enter)
email_entry.bind('<FocusOut>', email_leave)

email_frame = Frame(frame, width=285, height=2, bg='black')
email_frame.place(x=25, y=110)


def password_enter(entry):
    password_entry.delete(0, 'end')


def password_leave(entry):
    name = password_entry.get()
    if name == '':
        password_entry.insert(0, 'password')


password_entry = Entry(frame, width=25, fg='black', border=0, bg='white',
                       font=('Microsoft YaHei UI Light', 11))
password_entry.place(x=30, y=140)
password_entry.insert(0, 'password')
password_entry.bind('<FocusIn>', password_enter)
password_entry.bind('<FocusOut>', password_leave)

password_frame = Frame(frame, width=285, height=2, bg='black')
password_frame.place(x=25, y=170)

close_eye = PhotoImage(file='close_eye.png')
close_eye = close_eye.zoom(1, 1)
close_eye = close_eye.subsample(16, 16)

open_eye = PhotoImage(file='open_eye.png')
open_eye = open_eye.zoom(1, 1)
open_eye = open_eye.subsample(19, 19)

eye_button = Button(login_window, image=open_eye, bg='white', activebackground='white', fg='white', border=0,
                    cursor='hand2', command=hide_input)
eye_button.place(x=840, y=233)

forget_button = Button(login_window, text='Forgot Password?', bg='white', fg='black', border=0, cursor='hand2',
                       activebackground='white', font=('Microsoft YaHei UI Light', 9))
forget_button.place(x=780, y=280)

sign_in_button = Button(frame, width=39, pady=7, text='Sign in', bg='#57a1f8', fg='white', border=0, command=sign_in,
                        activebackground='#57a1f8')
sign_in_button.place(x=30, y=215)

label = Label(frame, text='Dont have an account?', fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
label.place(x=65, y=300)

sign_up_button = Button(frame, width=6, text='Sign up', border=0, bg='white', cursor='hand2', fg='#57a1f8')
sign_up_button.place(x=200, y=300)
login_window.mainloop()
