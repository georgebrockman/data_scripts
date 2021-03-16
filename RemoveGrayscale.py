import numpy as no
import matplotlib.pyplot as plt
import os
from PIL import Image

def is_gray_scale(img_path):
    """ Return True or False if image is Grayscale or not """
    img = Image.open(img_path).convert('RGB')
    w,h = img.size
    for i in range(w):
        for j in range(h):
            r,g,b = img.getpixel((i,j))
            if r != g != b: return False
    return True

def remove_grayscale(dir_path):
    """ Remove the grayscale images fromt he dataset """
    # add an if not clause to remove the DStore file from the list
    class_folders = [f for f in sorted(os.listdir(dir_path)) if not f.startswith('.')]
    # create empty lists for images and classes to iterate through
    images = []
    classes = []
    for i, c in enumerate(class_folders):
        # sort through files in class directories and check if JPEG
        images_per_class = [f for f in sorted(os.listdir(os.path.join(path, c))) if 'jpg' in f]

        for image_per_class in images_per_class:
            images.append(os.path.join(path, c, image_per_class))
            # the index will be the class label
            classes.append(i)

    for image in images:
        if is_gray_scale(image) is True:
            os.remove(image)

    return "Successfully removed grayscale images"
