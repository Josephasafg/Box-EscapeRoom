import time
from random import randint
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import StringVar
from tkinter import END
from PIL import ImageTk, Image


class Group:
    solving_password = "1966"

    def __init__(self, number: int, label: Label, name: str, code_label: Label, code_entry: Entry,
                 code_button: Button, start_button: Button, image_list, width, height, clock):
        self.time_string = time.strftime(clock.clock_to_str())
        self.stop_flag = False
        self.number = number
        self.label = label
        self._count = clock.time_to_seconds()
        self.deduce = 1
        self.name = name
        self.penalty = 600
        self.code_label = code_label
        self.code_entered = StringVar()
        self.code_entered.trace('w', self.limit_characters)
        self.code_entry = code_entry
        self.code_entry.configure(textvariable=self.code_entered)
        self.code_button = code_button
        self.start_button = start_button
        self.image_list = image_list
        self.width = width
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

    # def place_images(self):
    #     for _ in range(30):
    #         img = Label(self,)

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
            hour, seconds = divmod(self.count, 3600)
            minute, seconds = divmod(seconds, 60)
            if hour == 0 and minute == 0 and seconds == 0:
                self.stop_flag = True
            else:
                self.time_string = '{:02d}:{:02d}:{:02d}'.format(hour, minute, seconds)
                self.count -= self.deduce
                self.label.configure(text=self.name + self.time_string, fg="red")

    def check_code(self, i_code):
        is_true = False
        if i_code == self.solving_password:
            is_true = True
        else:
            if self.count < 600:
                self.time_string = '{:02d}:{:02d}:{:02d}'.format(0, 0, 0)
                self.label.configure(text=self.name + self.time_string, fg="white")
                self.count = 0
            else:
                self.count -= self.penalty
            self.code_entry.delete("0", END)

        return is_true
