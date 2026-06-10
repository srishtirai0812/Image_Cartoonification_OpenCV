# Cartoonification of an image

import cv2
import numpy as np
import sys
import matplotlib.pyplot as plt

import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

from Upload_Save import save

# hidden tkinter root
top = tk.Tk()
top.withdraw()


def cartoonify(image_path):

    image_org = cv2.imread(image_path)

    if image_org is None:
        print("Error! Please choose a valid image file")
        return

    image_org = cv2.cvtColor(image_org, cv2.COLOR_BGR2RGB)

    # grayscale
    image_gray = cv2.cvtColor(image_org, cv2.COLOR_RGB2GRAY)

    # blur
    gray_smooth = cv2.medianBlur(image_gray, 5)

    # edges
    image_edges = cv2.adaptiveThreshold(
        gray_smooth,
        255,
        cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY,
        9,
        9
    )

    # bilateral filter
    image_filter = cv2.bilateralFilter(
        image_org,
        9,
        300,
        300
    )

    # cartoon effect
    image_cartoon = cv2.bitwise_and(
        image_filter,
        image_filter,
        mask=image_edges
    )

    # resize for display
    image1 = cv2.resize(image_org, (600, 400))
    image2 = cv2.resize(image_gray, (600, 400))
    image3 = cv2.resize(gray_smooth, (600, 400))
    image4 = cv2.resize(image_edges, (600, 400))
    image5 = cv2.resize(image_filter, (600, 400))
    image6 = cv2.resize(image_cartoon, (600, 400))

    images = [
        image1,
        image2,
        image3,
        image4,
        image5,
        image6
    ]

    titles = [
        "Original",
        "Gray",
        "Blur",
        "Edges",
        "Filtered",
        "Cartoon"
    ]

    fig, axes = plt.subplots(
        3,
        2,
        figsize=(10, 8)
    )

    for i, ax in enumerate(axes.flat):
        if len(images[i].shape) == 2:
            ax.imshow(images[i], cmap="gray")
        else:
            ax.imshow(images[i])

        ax.set_title(titles[i])
        ax.axis("off")

    plt.tight_layout()

    save(image_cartoon, image_path)

    plt.show()