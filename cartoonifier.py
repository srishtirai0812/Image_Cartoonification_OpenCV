import cv2
import numpy as np


def cartoonify(image):
    img = np.array(image)

    if len(img.shape) == 2:
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)

    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    gray = cv2.medianBlur(gray, 5)

    edges = cv2.adaptiveThreshold(
        gray,
        255,
        cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY,
        9,
        9
    )

    color = cv2.bilateralFilter(img, 9, 300, 300)

    cartoon = cv2.bitwise_and(color, color, mask=edges)

    cartoon = cv2.cvtColor(cartoon, cv2.COLOR_BGR2RGB)

    return cartoon


def pencil_sketch(image):
    img = np.array(image)

    if len(img.shape) == 3:
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    else:
        gray = img

    invert = 255 - gray

    blur = cv2.GaussianBlur(invert, (21, 21), 0)

    sketch = cv2.divide(gray, 255 - blur, scale=256)

    return sketch


def watercolor(image):
    img = np.array(image)

    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    water = cv2.stylization(
        img,
        sigma_s=60,
        sigma_r=0.6
    )

    water = cv2.cvtColor(water, cv2.COLOR_BGR2RGB)

    return water