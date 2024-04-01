from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import colorchooser
from PIL import Image, ImageTk
from tkinter import filedialog


# image uploader function
def image_uploader():
    file_types = [("Image files", "*.png;*.jpg;*.jpeg")]
    path = filedialog.askopenfilename(filetypes=file_types)
    # if file is selected
    if len(path):
        img = Image.open(path)
        # img = img.resize((200, 200))
        pic = ImageTk.PhotoImage(Image.open(path))
        canvas.itemconfig(img_for_edit, image=pic, anchor='nw')
        label.image = pic


# set changes
def apply_changes():
    global font_list, water_mark_entry, font_size
    text = water_mark_entry.get()
    font = font_list.get()
    font_s = font_size.get()
    canvas.itemconfig(watermark, fill=color, font=(font, font_s, "normal"), text=text)


window = Tk()
window.title("Watermark")
window.config(padx=20, pady=20)
# window.minsize(width=800, height=500)

# image
canvas = Canvas(window, width=400)
sample_img = PhotoImage(file='sample.png')
img_for_edit = canvas.create_image(10, 10, image=sample_img, anchor='nw')
canvas.grid(column=0, row=0, columnspan=2)
label = Label(window)

# watermark
watermark = canvas.create_text(20, 20, text='A wonderful story', anchor='nw', font='Arial', fill='white')

# upload button
upload_button = Button(text="Upload Image", width=50, pady=10, command=image_uploader)
upload_button.grid(column=0, row=1, columnspan=2)

# watermark text
water_mark_label = Label(text="Water Maek Text:", pady=20)
water_mark_label.grid(column=0, row=2)

water_mark_entry = Entry(width=20)
water_mark_entry.grid(column=1, row=2)
water_mark_text = water_mark_entry.get()

# font
font_label = Label(text="Font", pady=10)
font_label.grid(column=0, row=3)

font_choices = ["Helvetica", "Arial", "Kalameh"]
font_list = ttk.Combobox(window, values=font_choices, width=16)
font_list.current(1)
font_list.grid(column=1, row=3)

# font size
font_size_label = Label(text="Font Size", pady=10)
font_size_label.grid(column=0, row=4)

font_size_value = StringVar()
font_size = ttk.Spinbox(window, from_=1.0, to=100.0, textvariable=font_size_value, width=17)
font_size.grid(column=1, row=4)

# opacity
opacity_label = Label(text="Opacity", pady=10)
opacity_label.grid(column=0, row=5)

opacity_value = StringVar()
opacity = ttk.Spinbox(window, from_=1.0, to=100.0, textvariable=opacity_value, width=17)
opacity.grid(column=1, row=5)

# color
color_sample = Canvas(window, width=100, height=20)
color_sample_rec = color_sample.create_rectangle(0, 0, 100, 100, fill="white", outline='white')
color_sample.grid(column=0, row=6)

color = "white"


def color_picker():
    global color
    watermark_color = colorchooser.askcolor(title="Choose color")
    color_sample.itemconfig(color_sample_rec, fill=watermark_color[1], outline=watermark_color[1])
    color = watermark_color[1]


color_button = Button(text="Choose Color", command=color_picker)
color_button.grid(column=1, row=6)

# Apply button
apply = Button(text="Apply", width=50, command=apply_changes)
apply.grid(column=0, row=7, columnspan=2, pady=20)

# Save button
save = Button(text="Save Image", width=50, pady=10)
save.grid(column=0, row=8, columnspan=2, pady=20)

window.mainloop()
