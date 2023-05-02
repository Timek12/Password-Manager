from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import pymysql
import time
from sign_in import validate_email
from sign_in import limegreen, forestgreen


def clear_entry_fields():
    email_entry.delete(0, END)
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    confirm_password_entry.delete(0, END)
    check_agreement.set(0)


def connect_database():
    # Check entry fields

    if email_entry.get() == '' or username_entry.get() == '' or password_entry.get() == '' or confirm_password_entry == '':
        messagebox.showerror('Error', 'All entry fields are required')
    elif password_entry.get() != confirm_password_entry.get():
        messagebox.showerror('Incorrect input data', 'Password mismatch')
    elif check_agreement.get() == 0:
        messagebox.showwarning('Incorrect input data', 'Acceptance of terms and conditions is required')
    elif not validate_email(email_entry.get()):
        messagebox.showerror('Incorrect input data', 'Incorrect email format')
    else:
        # establish connection to MySQL server
        try:
            connector = pymysql.connect(host='localhost', user='root', password='1234')
            my_cursor = connector.cursor()
        except:
            messagebox.showerror('Database error', 'Failed to connect to database, try again later')
            return

        # check if database already exists
        query = "SHOW DATABASES LIKE 'userdata'"
        my_cursor.execute(query)
        result = my_cursor.fetchone()

        if result is not None:
            # database already exists

            my_cursor.execute('use userdata')

        else:
            # create new database and table

            query = 'create database userdata'
            my_cursor.execute(query)
            query = 'use userdata2'
            my_cursor.execute(query)
            query = 'alter table data(id int auto_increment primary key not null, email varchar(40), username varchar(30), password varchar(20))'
            my_cursor.execute(query)
            print("Database and table created successfully.")

        query = 'select * from data where username=%s'
        my_cursor.execute(query, username_entry.get())

        # check if username already exists
        row = my_cursor.fetchone()
        if row is not None:
            messagebox.showerror('Incorrect input data', 'Username already exists')
        else:
            query = 'insert into data(email, username, password) values(%s, %s, %s)'
            my_cursor.execute(query, (email_entry.get(), username_entry.get(), password_entry.get()))
            connector.commit()
            connector.close()
            clear_entry_fields()
            messagebox.showinfo('Success', 'Registration is successful')
            time.sleep(3)

        signup_window.destroy()
        import sign_in


def login_page():
    signup_window.destroy()
    import sign_in


signup_window = Tk()
signup_window.geometry('1000x600')
signup_window.title('Registration Form')
signup_window.configure(bg="#fff")
signup_window.resizable(False, False)

image_open = Image.open("assets/img5.jpg")
image_open = image_open.resize((600, 600))
img = ImageTk.PhotoImage(image_open)

bg_label = Label(signup_window, image=img, bg='white')
bg_label.grid()

frame = Frame(signup_window, bg='white')
frame.place(x=550, y=60)

heading = Label(frame, text='Create an account', fg=forestgreen, bg='white',
                font=('Microsoft YaHei UI Light', 22, 'bold'))
heading.grid(row=0, column=0, padx=10, pady=10)

email_label = Label(frame, text='Email', font=('Microsoft YaHei UI Light', 11), bg='white')
email_label.grid(row=1, column=0, sticky='w', pady=4)

email_entry = Entry(frame, width=30, fg='black', border=1, bg='white', font=('Microsoft YaHei UI Light', 11))
email_entry.grid(row=2, column=0, sticky='w', pady=4)

username_label = Label(frame, text='Username', font=('Microsoft YaHei UI Light', 11), bg='white')
username_label.grid(row=3, column=0, sticky='w', pady=4)

username_entry = Entry(frame, width=30, fg='black', border=1, bg='white', font=('Microsoft YaHei UI Light', 11))
username_entry.grid(row=4, column=0, sticky='w', pady=4)

password_label = Label(frame, text='Password', font=('Microsoft YaHei UI Light', 11), bg='white')
password_label.grid(row=5, column=0, sticky='w', pady=4)

password_entry = Entry(frame, width=35, fg='black', border=1, bg='white', font=('Microsoft YaHei UI Light', 9))
password_entry.grid(row=6, column=0, sticky='w', pady=4)

confirm_password_label = Label(frame, text='Confirm Password', font=('Microsoft YaHei UI Light', 11), bg='white')
confirm_password_label.grid(row=7, column=0, sticky='w', pady=4)

confirm_password_entry = Entry(frame, width=35, fg='black', border=1, bg='white', font=('Microsoft YaHei UI Light', 9))
confirm_password_entry.grid(row=8, column=0, sticky='w', pady=4)

check_agreement = IntVar()

terms_confirmation = Checkbutton(frame, text='I agree to Terms & Conditions', font=('Microsoft YaHei UI Light', 9),
                                 bg='white', fg=forestgreen, activebackground='white', activeforeground=forestgreen,
                                 cursor='hand2', variable=check_agreement)
terms_confirmation.grid(row=9, column=0, sticky='w', pady=4)

sign_up_button = Button(frame, text='Sign up', width=35, height=2, font=('Microsoft YaHei UI Light', 12), bg=limegreen,
                        fg='white',
                        activebackground='#57a1f8', activeforeground='white', cursor='hand2', border=0,
                        command=connect_database)
sign_up_button.grid(row=10, column=0, sticky='w', pady=4)

no_account_label = Label(frame, text='Already have an account?', fg='black', bg='white',
                         font=('Microsoft YaHei UI Light', 9, 'bold'))
no_account_label.grid(row=11, column=0, sticky='w', pady=4)

sign_in_button = Button(frame, text='Sign in', height=2, font=('Microsoft YaHei UI Light', 10, 'bold'), bg='white',
                        fg=forestgreen, activebackground='white', activeforeground=forestgreen, cursor='hand2',
                        border=0, command=login_page)
sign_in_button.grid(row=11, column=0, padx=150, pady=4)

signup_window.mainloop()
