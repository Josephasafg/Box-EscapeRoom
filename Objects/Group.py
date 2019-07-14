import time
import math
from tkinter import Label
from tkinter import Button
from tkinter import END


class Group:
    solving_password = "1966"

    def __init__(self, number: int, group_label: Label, time_label: Label, name: str, code_entry,
                 code_button: Button, start_button: Button, canvas, width, height, clock, clue_buttons, dummies):
        self.time_string = time.strftime(clock.clock_to_str())
        self.images_coordinate = list()
        self.stop_flag = False
        self.number = number
        self.label = group_label
        self.time_label = time_label
        self.dummies = dummies
        self._count = clock.time_to_seconds()
        self.deduce = 1
        self.name = name
        self.penalty = 600
        self.code_entry = code_entry
        self.code_button = code_button
        self.start_button = start_button
        self.clue_buttons = clue_buttons
        self.canvas = canvas
        self.width = width
        self.height = height
        self.win_flag = False
        self.configure_music_buttons()
        self.configure_clue_buttons()
        self.second_counter = 0

    def configure_music_buttons(self):
        self.start_button.configure(command=self.start_clock)
        # self.pause_button.configure(command=self.pause_clock)

    def configure_clue_buttons(self):
        self.clue_buttons[0].configure(command=lambda: self.deduct_clue(self.clue_buttons[0]))
        self.clue_buttons[1].configure(command=lambda: self.deduct_clue(self.clue_buttons[1]))
        self.clue_buttons[2].configure(command=lambda: self.deduct_clue(self.clue_buttons[2]))
        # for button in self.clue_buttons:
        #     button.configure(command=lambda: self.deduct_clue(button))

    def deduct_clue(self, button):
        button.configure(state='disabled')
        amount_to_deduct = math.ceil(int(300 / 120))
        self.remove_image(amount_to_deduct)
        if self.count < 300:
            self.time_string = '{:02d}:{:02d}:{:02d}'.format(0, 0, 0)
            self.label.configure(text=self.name, fg="white")
            self.time_label.configure(text=self.time_string, fg='white')
            self.count = 0
        else:
            self.count -= 300

    def start_clock(self):
        if self.stop_flag:
            self.stop_flag = False
        else:
            self.stop_flag = True

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

    def remove_image(self, remove_amount=1):
        for _ in range(remove_amount):
            if self.images_coordinate:
                self.canvas.delete(self.images_coordinate.pop(0))

        if self.second_counter == 120:
            self.second_counter = 0

    def timer(self):
        if not self.stop_flag:
            hour, seconds = divmod(self.count, 3600)
            minute, seconds = divmod(seconds, 60)
            if self.win_flag:
                self.label.configure(text=self.name, fg="green")
                self.time_label.configure(text=self.time_string, fg='green')
                self.stop_flag = True
                return
            if hour == 0 and minute == 0 and seconds == 0:
                self.time_string = '{:02d}:{:02d}:{:02d}'.format(0, 0, 0)
                self.label.configure(text=self.name, fg="white")
                self.time_label.configure(text=self.time_string, fg='white')
                self.stop_flag = True
            else:
                self.time_string = '{:02d}:{:02d}:{:02d}'.format(hour, minute, seconds)
                self.count -= self.deduce
                self.label.configure(text=self.name, fg="red")
                self.time_label.configure(text=self.time_string, fg='red')
            self.second_counter += 1

            if self.second_counter == 120:
                self.remove_image()

    def check_code(self, i_code):
        if i_code == str(self.solving_password):
            self.win_flag = True
        else:
            if self.count < 600:
                image_to_remove = math.ceil(int(self.penalty / 120))
                self.remove_image(image_to_remove)
                self.time_string = '{:02d}:{:02d}:{:02d}'.format(0, 0, 0)
                self.label.configure(text=self.name, fg="white")
                self.time_label.configure(text=self.time_string, fg='white')
                self.count = 0
            elif i_code == 'ENTER CODE':
                return self.win_flag
            else:
                image_to_remove = math.ceil(int(self.penalty / 120))
                self.remove_image(image_to_remove)
                self.count -= self.penalty
            self.code_entry.delete("0", END)

        return self.win_flag
