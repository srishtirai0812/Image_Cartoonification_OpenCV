# Upload and Save the cartoonified image

import cv2
import easygui
import tkinter as tk
from tkinter import messagebox
import os


def upload():
    from Image_Cartoonification import cartoonify

    image_path = easygui.fileopenbox()

    if image_path:
        cartoonify(image_path)


def save(image_cartoon, image_path):

    path1 = os.path.dirname(image_path)
    name_old = os.path.basename(image_path)

    name_new = "Cartoonified_Image-" + name_old
    path = os.path.join(path1, name_new)

    cv2.imwrite(path, cv2.cvtColor(image_cartoon, cv2.COLOR_RGB2BGR))

    messagebox.showinfo(
        title="Saved",
        message=f"Image saved as\n{name_new}\n\nLocation:\n{path}"
    )