# import tkinter as tk

# root = tk.Tk()
# root.title('Expense Tracker Application')
# root.geometry("500x200")
# label = tk.Label(root, text="Hello, World!", font=("Arial", 24), fg="white", bg="blue", padx=20, pady=10)

# # Add the label to the window
# label.pack()
# # label.pack()
# root.mainloop()

# from tkinter import *
# master = Tk()
# w = Scale(master, from_=0, to=42)
# w.pack()
# w = Scale(master, from_=0, to=200, orient=HORIZONTAL)
# w.pack()
# mainloop()

from tkinter import *


top = Tk()
top.geometry("450x300")

# the label for user_name
user_name = Label(top,
				text = "Username").place(x = 40,
										y = 60)

# the label for user_password
user_password = Label(top,
					text = "Password").place(x = 40,
											y = 100)

submit_button = Button(top,
					text = "Submit").place(x = 40,
											y = 130)

user_name_input_area = Entry(top,
							width = 30).place(x = 110,
											y = 60)

user_password_entry_area = Entry(top,
								width = 30).place(x = 110,
												y = 100)
	
top.mainloop()
