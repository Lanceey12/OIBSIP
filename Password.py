import string
from tkinter import *
from random import randint
from tkinter import messagebox

root = Tk()
root.title('Strong Password Generator')
root.geometry("500x500")
root.resizable(True, True)


def generate_password():
    pw_length_str = user_pw.get()
    if not pw_length_str.isdigit():
        messagebox.showerror("Error", "Please enter a valid integer for password length.")
        return

    pw_length = int(pw_length_str)
    if pw_length <= 0:
        messagebox.showerror("Error", "Password length must be greater than 0.")
        return

    user_password = ''

    for i in range(pw_length):
        user_password += chr(randint(33, 126))

    pw_answer.delete(0, 'end')
    pw_answer.insert(0, user_password)


#function to copy to clipboard
def copy():
    root.clipboard_clear()
    root.clipboard_append(pw_answer.get())
    messagebox.showinfo('Copied to clipboard', pw_answer.get())


# label frame
label_frame = LabelFrame(root, text="How Many Characters?")
label_frame.pack(pady=20)

# Entry box
user_pw = Entry(label_frame, font=("Bebas kai", 24))
user_pw.pack(pady=20, padx=20)

# Generated password entry box
pw_answer = Entry(label_frame, font=("Bebas kai", 24))
pw_answer.pack(pady=20, padx=20)

# Frames for all the Buttons
frame = Frame(root)
frame.pack(pady=20)

# Buttons
pwd_button = Button(frame, text="Generate Password", font=("Bebas kai", 24), command=generate_password)
pwd_button.grid(row=0, column=0, padx=10)

clipbd_button = Button(frame, text="Copy To Clipboard", font=("Bebas kai", 24), command=copy)
clipbd_button.grid(row=0, column=1, padx=10)

root.mainloop()
