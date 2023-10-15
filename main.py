
a=int(input())
while a > 0:
    import time
    time.sleep(1)
    print(a)
    a = a-1
print("Бум")
from tkinter import *
def change_color():
    current_color = box.cget("background")
    next_color = "black" if current_color == "red" else "red"
    box.config(background=next_color)
    root.after(100, change_color)
root = Tk()
box = Text(root, background="black")
box.pack()
change_color()
root.mainloop()