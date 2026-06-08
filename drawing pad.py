from tkinter import *

root = Tk()
root.title("Drawing Pad")
root.geometry("800x600")

canvas = Canvas(root, bg="white", width=800, height=550)
canvas.pack()

def draw(event):
    x, y = event.x, event.y
    canvas.create_oval(x, y, x+4, y+4, fill="black", outline="black")

canvas.bind("<B1-Motion>", draw)

def clear_canvas():
    canvas.delete("all")

clear_button = Button(root, text="Clear Canvas", command=clear_canvas)
clear_button.pack(pady=5)

root.mainloop()