import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import re
import subprocess


class App:
    def __init__(self, root):
        self.root = root
        self.width = 630
        self.height = 360
        self.background_label = None
        self.email_entry = None
        self.password_entry = None
        self.error_label = None
        self.background_image = None

    def validate_email(self, email):
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return bool(re.match(pattern, email))

    def submit_form(self):
        """
        Validate the email and perform the desired action.
        """
        email = self.email_entry.get()
        password = self.password_entry.get()

        if not self.validate_email(email):
            self.error_label.config(text="Invalid email")
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

    def create_gui(self):
        # create the background image label using place()
        image = Image.open("background3.jpg")
        self.background_image = ImageTk.PhotoImage(image)
        background_label = tk.Label(self.root, image=self.background_image)
        background_label.place(relx=0, rely=0, relwidth=1, relheight=1)
        grid = 160
        # create the email label and entry field using grid()
        email_label = tk.Label(self.root, text="Email:")
        email_label.place(x=grid * 1, y=grid)

        email_entry = tk.Entry(self.root, highlightthickness=0)
        email_entry.place(x=1.5 * grid, y=grid)

        # create the password label and entry field using grid()
        password_label = tk.Label(self.root, text="Password:")
        password_label.place(x=grid * 1, y=1.2 * grid)

        password_entry = tk.Entry(self.root, show="*")
        password_entry.place(x=1.5 * grid, y=1.2 * grid)

        # create the submit button using place()
        submit_button = tk.Button(self.root, text="Submit", command=self.submit_form)
        submit_button.place(x=grid * 1.5, y=grid * 1.4)

        # create the error label using place()
        error_label = tk.Label(self.root, fg="red")
        error_label.place(x=grid * 2.3, y=grid)

        # set the size of the window and run the main loop
        self.root.geometry(f"{self.width}x{self.height}")


def main():
    root = tk.Tk()
    app = App(root)
    App.create_gui(app)
    root.mainloop()


if __name__ == '__main__':
    main()
