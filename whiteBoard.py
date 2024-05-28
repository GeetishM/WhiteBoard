from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import ttk
import tkinter as tk
from tkinter import filedialog
import os
from tkinter.colorchooser import askcolor
from tkinter import ttk, filedialog

root = tk.Tk()
root.title('WHITE BOARD')
root.geometry("1920x1080")
root.config(bg="#e9ecef")
root.resizable(True, True)

current_x = 0
current_y = 0
color = "black"

def locate_xy(event):
    global current_x, current_y
    current_x = event.x
    current_y = event.y

def addline(event):
    global current_x, current_y

    canvas.create_line((current_x, current_y, event.x, event.y), width=get_current_value(),
                       fill=color, capstyle=tk.ROUND, smooth=True)
    current_x, current_y = event.x, event.y

def show_color(new_color):
    global color
    color = new_color

def new_canvas():
    canvas.delete('all')
    display_pallete()

def erase_within_radius(event):
    x, y = event.x, event.y
    radius = 20
    canvas.create_oval(x - radius, y - radius, x + radius, y + radius, outline='', fill='white')


def insertimage():
    global filename
    global f_img

    filename=filedialog.askopenfilename(initialdir=os.getcwd(),title='Select image file',
                                        filetype=(("PNG file","*.png"),("All file","new.txt")))
    f_img=tk.PhotoImage(file=filename)
    my_img=canvas.create_image(180,50,image=f_img)
    root.bind("<B3-Motion>",my_callback)
def my_callback(event):
    global f_img
    f_img= tk.PhotoImage(file=filename)
    my_img=canvas.create_image(event.x,event.y,image=f_img)
def get_current_value():
    return '{: .2f}'.format(current_value.get())

def slider_changed(event):
    value_label.configure(text=get_current_value())

current_value = tk.DoubleVar()


#icon
image_icon = tk.PhotoImage(file="F:\ML projects\Whiteboard\images (1).png")
root.iconphoto(False, image_icon)

##sidebar
color_box = tk.PhotoImage(file="F:\ML projects\Whiteboard\color section.png")
tk.Label(root, image=color_box, bg="#e9ecef").place(x=10, y=20)

eraser = tk.PhotoImage(file="F:\ML projects\Whiteboard\eraser.png")
tk.Button(root, image=eraser, bg="#e9ecef", command=new_canvas).place(x=30, y=400)

importimage = tk.PhotoImage(file="addimage.png")
tk.Button(root, image=importimage, bg="white",command=insertimage).place(x=30, y=450)

###color
colors = tk.Canvas(root, bg="#fff", width=37, height=300, bd=0)
colors.place(x=30, y=60)

def display_pallete():
    id = colors.create_rectangle((10, 10, 30, 30), fill="black")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('black'))

    id = colors.create_rectangle((10, 40, 30, 60), fill="#e03131")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('#e03131'))

    id = colors.create_rectangle((10, 70, 30, 90), fill="red")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('red'))

    id = colors.create_rectangle((10, 100, 30, 120), fill="#1971c2")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('#1971c2'))

    id = colors.create_rectangle((10, 130, 30, 150), fill="black")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('black'))

    id = colors.create_rectangle((10, 160, 30, 180), fill="black")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('black'))

    id = colors.create_rectangle((10, 190, 30, 210), fill="black")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('black'))

display_pallete()

## main screen
canvas = tk.Canvas(root, width=1410, height=720, background="white", cursor="hand2")
canvas.place(x=100, y=10)

canvas.bind("<Button-1>", locate_xy)
canvas.bind("<B1-Motion>", addline)

###slider
slider = ttk.Scale(root, from_=0, to=10, orient="horizontal", command=slider_changed, variable=current_value)
slider.place(x=30, y=740)

value_label = ttk.Label(root, text=get_current_value())
value_label.place(x=27, y=760)

## Erase Within Radius Binding
canvas.bind("<B3-Motion>", erase_within_radius)

root.mainloop()