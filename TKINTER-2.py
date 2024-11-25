import tkinter
from tkinter import ttk, messagebox

root = tkinter.Tk()

# root = tkinter.Tk(className="My Window")
root.title("My Window")
root.geometry("400x400")
root.resizable(width=False, height=False)
root.configure(bg="#0c4953")


def show_result():
    # messagebox.showwarning("Result", "Successfully Logged In")
    # messagebox.showwarning("Result", "Successfully Logged In")
    messagebox.showinfo("Result", "Successfully Logged In")


submit_button = tkinter.Button(root, text="Log in", command=show_result)
submit_button.pack()

root.mainloop()
