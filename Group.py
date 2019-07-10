import time
from random import randint
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import StringVar
from tkinter import END
from PIL import ImageTk, Image


class Group:
    def __init__(self, number: int, label: Label, name: str, code_label: Label, code_entry: Entry,
                 code_button: Button, penalty: int, start_button: Button, image_list, width, height):
        self.time_string = time.strftime("60:00:00")
        self.stop_flag = False
        self.number = number
        self.label = label
        self._count = 3600
        self.deduce = 1
        self.name = name
        self.penalty = penalty
        self.code_label = code_label
        self.code_entered = StringVar()
        self.code_entered.trace('w', self.limit_characters)
        self.code_entry = code_entry
        self.code_entry.configure(textvariable=self.code_entered)
        self.code_button = code_button
        self.start_button = start_button
        self.image_list = image_list
        self.width= width
        self.height = height
        self.configure_music_buttons()

    def configure_music_buttons(self):
        self.start_button.configure(command=self.start_clock)
        # self.pause_button.configure(command=self.pause_clock)

    def start_clock(self):
        if self.stop_flag:
            self.stop_flag = False
        else:
            self.stop_flag = True

    def place_images(self):
        for _ in range(30):
            img = Label(self,)

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value

    def limit_characters(self, *args):
        value = self.code_entered.get()
        if len(value) > 4:
            self.code_entered.set(value[:4])

    def timer(self):
        if not self.stop_flag:
            minute, seconds = divmod(self.count, 60)
            if minute == 60:
                hour = 60
                self.time_string = '{:02d}:{:02d}:{:02d}'.format(hour, seconds, seconds)
            else:
                hour = 0
                self.time_string = '{:02d}:{:02d}:{:02d}'.format(hour, minute, seconds)

            self.count -= self.deduce
            self.label.configure(text=self.name + self.time_string, fg="red")
            # self.after(1000, self.timer)

    def check_code(self, i_code):
        is_true = False
        if i_code == "1966":
            is_true = True
        else:
            self.count -= self.penalty
            self.code_entry.delete("0", END)

        return is_true
