import tkinter as tk
from PIL import Image, ImageTk
import re
import subprocess

global email_entry, password_entry, error_label


def validate_email(email):
    """
    Validate the email using a regular expression.
    """
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))


def submit_form():
    """
    Validate the email and perform the desired action.
    """
    email = email_entry.get()
    password = password_entry.get()

    if not validate_email(email):
        error_label.config(text="Invalid email")
        return
    else:
        password_bytes = password.encode('utf-8')
        cmd = ['C:/Users/HP/mingw64/bin/x86_64-w64-mingw32-gcc.exe', '-shared', '-o', 'encrypt.dll', 'encrypt.c']
        subprocess.run(cmd)
        cmd = ['C:/Users/HP/mingw64/bin/x86_64-w64-mingw32-gcc.exe', '-o', 'main.exe', 'main.c', 'encrypt.dll']
        subprocess.run(cmd)
        cmd = ['./main.exe', password_bytes]
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        if result.returncode != 0:
            print("Error:", result.stdout.decode('utf-8'))
        else:
            encrypted_password = result.stdout.decode('utf-8').strip()
            # encrypted_password_hex = binascii.hexlify(encrypted_password_bytes).decode('ascii')
            print("Encrypted password is:", encrypted_password)


def main():
    print('start')
    root = tk.Tk()

    width = 600
    height = 1064

    # create the background image label using place()
    image = Image.open("background2.png")
    photo = ImageTk.PhotoImage(image)
    background_label = tk.Label(root, image=photo)
    background_label.place(relx=0, rely=0, relwidth=1, relheight=1)
    grid = 150
    # create the email label and entry field using grid()
    email_label = tk.Label(root, text="Email:")
    email_label.place(x=grid, y=grid)
    global email_entry
    email_entry = tk.Entry(root)
    email_entry.place(x=1.5*grid, y=grid)

    # create the password label and entry field using grid()
    password_label = tk.Label(root, text="Password:")
    password_label.place(x=grid, y=1.2*grid)
    global password_entry
    password_entry = tk.Entry(root, show="*")
    password_entry.place(x=1.5*grid, y=1.2*grid)


    # create the submit button using place()
    submit_button = tk.Button(root, text="Submit", command=submit_form)
    submit_button.place(x=grid*1.5, y=grid*1.4)


    # create the error label using place()
    error_label = tk.Label(root, fg="red")
    error_label.place(x=grid*2.3, y=grid)


    # set the size of the window and run the main loop
    root.geometry(f"{width}x{height}")

    root.mainloop()



if __name__ == '__main__':
    main()
