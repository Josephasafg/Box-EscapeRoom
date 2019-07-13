from random import randint
from PIL import ImageTk, Image
from tkinter import Label, Canvas
from tkinter import filedialog, X, Y, BOTH, N, W, S, E, CENTER, NE


def add_photo(photo_entry):
    filename = filedialog.askopenfilename()
    photo_entry.insert(0, filename)


def place_images(group, amount_of_images):
    if group.width < 1000:
        group.width *= 2
    for image in range(amount_of_images):
        rand_x = randint(0, group.width)
        rand_y = randint(0, group.height)
        image_id = group.canvas.create_image(rand_x, rand_y, image=group.canvas.image, anchor=CENTER)
        group.images_coordinate.append(image_id)
    group.canvas.pack(expand=True, fill=BOTH)
        # group.image_list[image].place(x=rand_x, y=rand_y)


def load_images(canvas: Canvas, photo_path):
    load = Image.open(photo_path)
    canvas.image = ImageTk.PhotoImage(load)
    return canvas


# def create_images(canvas):
#     image_list = list()
#     for _ in range(10):
#         # canvas.create_image()
#         # img = Label(frame, image=rendered_image)
#         # img.image = rendered_image
#         image_list.append(canvas)
#     return image_list
