import re
import secrets
import smtplib
import string
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tkinter import *
from tkinter import messagebox

import pymysql
from PIL import Image, ImageTk

limegreen = '#32CD32'
green = '#008000'
forestgreen = '#228B22'


def clear_entry_fields():
    email_entry.delete(0, END)
    password_entry.delete(0, END)


def signup_page():
    login_window.destroy()


def hide_input():
    global open_eye, close_eye
    open_eye = Image.open('assets/close_eye.png')
    open_eye = open_eye.resize((30, 30), Image.ANTIALIAS)
    open_eye = ImageTk.PhotoImage(open_eye)
    eye_button.config(image=open_eye)
    password_entry.config(show='*')

    eye_button.config(command=show_input)


def show_input():
    global open_eye, close_eye
    close_eye = Image.open('assets/open_eye.png')
    close_eye = close_eye.resize((35, 35), Image.ANTIALIAS)
    close_eye = ImageTk.PhotoImage(close_eye)
    eye_button.config(image=close_eye)
    password_entry.config(show='')

    eye_button.config(command=hide_input)


def validate_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))


def sign_in_user():
    if email_entry.get() == '' or password_entry.get() == '':
        messagebox.showerror('Incorrect input data', 'All entry fields are required')
    else:
        try:
            connector = pymysql.connect(host='localhost', user='root', password='1234')
            my_cursor = connector.cursor()
        except pymysql.err.OperationalError as e:
            messagebox.showerror('Database error', f'Failed to connect to database: {str(e)}')
            return
        except pymysql.err.InternalError as e:
            messagebox.showerror('Database error', f'Error executing query: {str(e)}')
            return
        except pymysql.err.ProgrammingError as e:
            messagebox.showerror('Programming error', f'Error in programming: {str(e)}')
            return

        query = 'use userdata'
        my_cursor.execute(query)
        query = 'select * from data where email=%s and password=%s'
        my_cursor.execute(query, (email_entry.get(), password_entry.get()))
        row = my_cursor.fetchone()

        # validate email and password
        if row is None:
            messagebox.showerror('Incorrect input data', 'Invalid email or password')
        else:
            messagebox.showinfo('Success', 'Login successful')
            clear_entry_fields()
            login_window.destroy()


def send_email(to_email, subject, body):
    # set up the SMTP server
    smtp_server = "smtp.gmail.com"
    smtp_port = 587  # or 465 for SSL/TLS encrypted connection
    sender_email = "your_email@gmail.com"
    sender_password = "your_email_password"
    receiver_email = to_email

    # create a message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # add body to the message
    message.attach(MIMEText(body, "plain"))

    # send the message
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, message.as_string())
            global f_submit_clicked
            f_submit_clicked = True

    except smtplib.SMTPConnectError:
        messagebox.showerror('Connection failure', 'Failed to connect to the SMTP server')
        return
    except smtplib.SMTPAuthenticationError:
        messagebox.showerror('Connection failure', 'SMTP authentication error occurred')


def reset_password(secret_code):
    global f_window
    if f_password_entry.get() == '' or f_code_entry.get() == '' or f_password_entry.get() == '' \
            or f_confirm_password_entry.get() == '':
        messagebox.showerror('Incorrect input data', 'All entry fields are required')
    elif f_password_entry.get() != f_confirm_password_entry.get():
        messagebox.showerror('Incorrect input data', 'Password mismatch')
    elif not validate_email(f_email_entry.get()):
        messagebox.showerror('Incorrect input data', 'Invalid email format')
    else:
        if f_code_entry.get() == secret_code:
            messagebox.showinfo('Success', 'Successfully changed password')
            time.sleep(5)
            if f_window is not None:
                f_window.destroy()
        else:
            messagebox.showerror('Authentication error', '')
            time.sleep(5)
            f_window.destroy()


def change_password():
    global f_email_entry, f_code_entry, f_password_entry, f_confirm_password_entry, f_submit_clicked, f_window

    f_window = Toplevel()
    f_window.geometry('800x500')
    f_window.title('Change password')
    f_window.configure(bg="#fff")
    f_window.resizable(False, False)

    f_image_open = Image.open("assets/img4.jpg")
    f_image_open = f_image_open.resize((450, 450))
    f_img = ImageTk.PhotoImage(f_image_open)

    f_bg_label = Label(f_window, image=f_img, bg='white')
    f_bg_label.grid()

    f_frame = Frame(f_window, width=350, height=350, bg="white")
    f_frame.place(x=450, y=60)

    f_heading = Label(f_frame, text='Change password', fg=forestgreen, bg='white',
                      font=('Microsoft YaHei UI Light', 24, 'bold'))
    f_heading.grid(row=0, column=0)

    f_email_label = Label(f_frame, text='Email', font=('Microsoft YaHei UI Light', 11), bg='white')
    f_email_label.grid(row=1, column=0, sticky='w', pady=4)

    f_email_entry = Entry(f_frame, width=30, fg='black', border=1, bg='white', font=('Microsoft YaHei UI Light', 11))
    f_email_entry.grid(row=2, column=0, sticky='w', pady=4)

    alphabet = string.ascii_uppercase + string.digits
    secret_code = ''.join(secrets.choice(alphabet) for _ in range(8))
    body = f'Hello,\n\nYou have requested to reset your password. Please enter the following verification code on the password reset page:\n\n{secret_code}\n\nIf you did not request a password reset, please disregard this email.\n\nThank you,'

    f_submit_button = Button(f_frame, text='Send code', width=10, height=2,
                             font=('Microsoft YaHei UI Light', 10, 'bold'),
                             bg=limegreen, fg='white', activebackground=limegreen, activeforeground='white',
                             cursor='hand2', border=0,
                             command=lambda: send_email(f_email_entry.get(), 'Email confirmation', body))
    f_submit_button.grid(row=2, column=0, sticky='w', padx=250, pady=4)

    # Check if the submit button has been clicked
    if f_submit_clicked:
        f_code_label = Label(f_frame, text='Email code', font=('Microsoft YaHei UI Light', 11), bg='white')
        f_code_label.grid(row=3, column=0, sticky='w', pady=4)

        f_code_entry = Entry(f_frame, width=30, fg='black', border=1, bg='white', font=('Microsoft YaHei UI Light', 11))
        f_code_entry.grid(row=4, column=0, sticky='w', pady=4)

        f_password_label = Label(f_frame, text='Password', font=('Microsoft YaHei UI Light', 11), bg='white')
        f_password_label.grid(row=5, column=0, sticky='w', pady=4)

        f_password_entry = Entry(f_frame, width=30, fg='black', border=1, bg='white',
                                 font=('Microsoft YaHei UI Light', 11))
        f_password_entry.grid(row=6, column=0, sticky='w', pady=4)

        f_confirm_password_label = Label(f_frame, text='Confirm Password', font=('Microsoft YaHei UI Light', 11),
                                         bg='white')
        f_confirm_password_label.grid(row=7, column=0, sticky='w', pady=4)

        f_confirm_password_entry = Entry(f_frame, width=30, fg='black', border=1, bg='white',
                                         font=('Microsoft YaHei UI Light', 11))
        f_confirm_password_entry.grid(row=8, column=0, sticky='w', pady=4)

        f_reset_button = Button(f_frame, text='Reset password', width=30, height=2,
                                font=('Microsoft YaHei UI Light', 12),
                                bg=limegreen, fg='white', activebackground=limegreen, activeforeground='white',
                                cursor='hand2', border=0, command=lambda: reset_password(secret_code))
        f_reset_button.grid(row=9, column=0, sticky='w', pady=6)
    f_window.mainloop()


def password_enter(entry):
    password_entry.delete(0, 'end')


def password_leave(entry):
    name = password_entry.get()
    if name == '':
        password_entry.insert(0, 'password')


def email_enter(event):
    email_entry.delete(0, 'end')


def email_leave(event):
    name = email_entry.get()
    if name == '':
        email_entry.insert(0, 'e-mail')


login_window = Tk()

login_window.geometry('1000x600')
login_window.title('Login Form')
login_window.configure(bg="#fff")
login_window.resizable(False, False)

image_open = Image.open("assets/img4.jpg")
image_open = image_open.resize((600, 600))
img = ImageTk.PhotoImage(image_open)

Label(login_window, image=img, bg='white').place(x=50, y=50, height=500, width=550)

frame = Frame(login_window, width=350, height=350, bg="white")
frame.place(x=570, y=100)

heading = Label(frame, text='Sign in', fg=forestgreen, bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=110, y=5)

email_entry = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
email_entry.place(x=30, y=80)
email_entry.insert(0, 'e-mail')
email_entry.bind('<FocusIn>', email_enter)
email_entry.bind('<FocusOut>', email_leave)

email_frame = Frame(frame, width=285, height=2, bg='black')
email_frame.place(x=25, y=110)

password_entry = Entry(frame, width=25, fg='black', border=0, bg='white',
                       font=('Microsoft YaHei UI Light', 11))
password_entry.place(x=30, y=140)
password_entry.insert(0, 'password')
password_entry.bind('<FocusIn>', password_enter)
password_entry.bind('<FocusOut>', password_leave)

password_frame = Frame(frame, width=285, height=2, bg='black')
password_frame.place(x=25, y=170)

close_eye = PhotoImage(file='assets/close_eye.png')
close_eye = close_eye.zoom(1, 1)
close_eye = close_eye.subsample(16, 16)

open_eye = PhotoImage(file='assets/open_eye.png')
open_eye = open_eye.zoom(1, 1)
open_eye = open_eye.subsample(19, 19)

eye_button = Button(login_window, image=open_eye, bg='white', activebackground='white', fg='white', border=0,
                    cursor='hand2', command=hide_input)
eye_button.place(x=840, y=233)

forgot_button = Button(login_window, text='Forgot Password?', bg='white', fg='black', border=0, cursor='hand2',
                       activebackground='white', font=('Microsoft YaHei UI Light', 9), command=change_password)
forgot_button.place(x=780, y=280)

sign_in_button = Button(frame, width=39, pady=7, text='Sign in', bg=limegreen, fg='white', border=0,
                        command=sign_in_user, activebackground=limegreen)
sign_in_button.place(x=30, y=215)

no_account_label = Label(frame, text='Dont have an account?', fg='black', bg='white',
                         font=('Microsoft YaHei UI Light', 9))
no_account_label.place(x=65, y=300)

sign_up_button = Button(frame, width=6, text='Sign up', border=0, bg='white', cursor='hand2', fg=forestgreen,
                        command=signup_page)
sign_up_button.place(x=200, y=300)
login_window.mainloop()
