import tkinter as tk
from tkinter import Button

from Upload_Save import upload

top = tk.Tk()
top.geometry("400x400")
top.title("Image Cartoonification")
top.configure(background="white")

upload_btn = Button(
    top,
    text="Cartoonify an Image",
    command=upload,
    padx=10,
    pady=5,
    bg="#364156",
    fg="white",
    font=("calibri", 12, "bold")
)

upload_btn.pack(pady=120)

top.mainloop()