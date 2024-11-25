import tkinter

root = tkinter.Tk()

# root = tkinter.Tk(className="My Window")
root.title("My Window")
root.geometry("400x400")
root.resizable(width=False, height=False)
root.configure(bg="#0c4953")

welcome_message = tkinter.Label(root, text="Welcome", bg="black", fg="white")
welcome_message.pack(anchor="center", fill="x")

root.mainloop()
