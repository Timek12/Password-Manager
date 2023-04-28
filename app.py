from tkinter import*
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()

root.geometry('1000x600')
root.title('Registration Form')
root.configure(bg="#fff")
root.resizable(False, False)

def sign_in():
    email = email_entry.get()
    password = password_entry.get()
    if email == 'admin@gmail.com' and password == 'admin123':
        screen = Toplevel(root)
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

Label(root, image=img, bg='white').place(x=50, y=50, height=500, width=550)

frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=570, y=100)

heading = Label(frame, text='Sign in', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=110, y=5)


def on_enter(entry):
    email_entry.delete(0, 'end')


def on_leave(entry):
    name = email_entry.get()
    if name == '':
        email_entry.insert(0, 'e-mail')


email_entry = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
email_entry.place(x=30, y=80)
email_entry.insert(0, 'e-mail')
email_entry.bind('<FocusIn>', on_enter)
email_entry.bind('<FocusOut>', on_leave)


Frame(frame, width=285, height=2, bg='black').place(x=25, y=110)


def on_enter(entry):
    password_entry.delete(0, 'end')


def on_leave(entry):
    name = password_entry.get()
    if name == '':
        password_entry.insert(0, 'password')


password_entry = Entry(frame, width=25, fg='black', border=0, show='*', bg='white', font=('Microsoft YaHei UI Light', 11))
password_entry.place(x=30, y=140)
password_entry.insert(0, 'password')
password_entry.bind('<FocusIn>', on_enter)
password_entry.bind('<FocusOut>', on_leave)


Frame(frame, width=285, height=2, bg='black').place(x=25, y=170)


Button(frame, width=39, pady=7, text='Sign in', bg='#57a1f8', fg='white', border=0, command=sign_in).place(x=30, y=204)
label = Label(frame, text='Dont have an account?', fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
label.place(x=65, y=255)


sign_up = Button(frame, width=6, text='Sign up', border=0, bg='white', cursor='hand2', fg='#57a1f8')
sign_up.place(x=205, y=255)
root.mainloop()
