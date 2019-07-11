from random import randint
from PIL import ImageTk, Image
from tkinter import Label
from tkinter import filedialog


def add_photo(photo_entry):
    filename = filedialog.askopenfilename()
    photo_entry.insert(0, filename)


def place_images(group):
    for image in range(30):
        rand_x = randint(0, group.width)
        rand_y = randint(0, group.height)
        group.image_list[image].place(x=rand_x, y=rand_y)


def load_images(photo_path):
    load = Image.open(photo_path)
    render = ImageTk.PhotoImage(load)
    return render


def create_images(frame, rendered_image):
    image_list = list()
    for _ in range(30):
        img = Label(frame, image=rendered_image)
        img.image = rendered_image
        image_list.append(img)
    return image_list
