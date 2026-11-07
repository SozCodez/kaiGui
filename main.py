import tkinter as tk

text0 = "Hello World!"
root = tk.Tk()

myLabel = Label(root, text=text0)
myLabel.pack()

root.mainLoop()
