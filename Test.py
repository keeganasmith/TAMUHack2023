from tkinter import *

win = Tk()
# Set the Geometry
win.geometry("750x250")
def print_width():
   print("The width of Tkinter window:", win.winfo_width())
   print("The height of Tkinter window:", win.winfo_height())
# Create a Label
Label(win, text="Click the below Button to Print the Height and width of the Screen", font=('Helvetica 10 bold')).pack(pady=20)
# Create a Button for print function
Button(win, text="Click", command=print_width).pack(pady=10)
win.mainloop()