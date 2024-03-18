import tkinter as tk

def display_message():
    label.config(text = "Hello GUI!!!")

# Creating the main application window
root = tk.Tk()
root.title("Simple GUI Example")

# Create a label widget
label = tk.Label(root, text = "Welcome to my GUI")
label.pack(pady = 10)

# Create a button widget
button = tk.Button(root, text = "Click Me!!!", command=display_message())
button.pack()

# Start the GUI Event Loop
root.mainloop()
