import pygame
import time
import tkinter.messagebox
from typing import Tuple
from tkinter import *
from tkinter import ttk
from Group import Group

LARGE_FONT = ("verdana", 16)


class Game(Frame):
    amount_of_groups = 1
    penalty = 300
    group_name_list = list()

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.count = 3600
        self.configure(background='black')
        self.time_string = time.strftime("60:00:00")
        self.group_name = "Group "
        self.stop_flag = False
        pygame.mixer.init()
        pygame.mixer.music.load("Music/DY.ogg")
        self.group_list = list()
        self.pause_button = ttk.Button(self, text="Pause",
                                       command=self.stop_game)
        self.start_button = ttk.Button(self, text="Start",
                                       command=self.begin_game)
        self.create_groups()

    @classmethod
    def set_name_list(cls, value):
        cls.group_name_list = value

    @classmethod
    def get_name_list(cls):
        return cls.group_name_list

    @classmethod
    def get_penalty(cls):
        return cls.penalty

    @classmethod
    def updated_amount(cls):
        return cls.amount_of_groups

    def design_groups(self):
        for index, group in enumerate(self.group_list):
            if index % 2 == 0:
                group.label.grid(row=0, column=index * 4, padx=10, pady=10, sticky=E)
                group.code_label.grid(row=1, column=index * 4)
                group.code_entry.grid(row=1, column=index * 4 + 1)
                group.code_button.grid(row=2, column=index * 4 + 1)
                group.start_button.grid(row=3, column=index * 4 + 1)
                group.pause_button.grid(row=3, column=index * 4 + 2)
            else:
                group.label.grid(row=4, column=(index - 1) * 4, padx=10, pady=10, sticky=W)
                group.code_label.grid(row=5, column=(index - 1) * 4)
                group.code_entry.grid(row=5, column=(index - 1) * 4 + 1)
                group.code_button.grid(row=6, column=(index - 1) * 4 + 1)
                group.start_button.grid(row=7, column=(index - 1) * 4 + 1)
                group.pause_button.grid(row=7, column=(index - 1) * 4 + 2)

    def create_music_buttons(self) -> Tuple[Button, Button]:
        start_button = ttk.Button(self, text="Play")
        pause_button = ttk.Button(self, text="Pause")
        return start_button, pause_button

    def create_groups(self):
        group_amount = self.updated_amount()
        name_list = self.get_name_list()
        for index, group_name in zip(range(1, group_amount + 1), name_list):
            group_name = group_name + ": "
            label = Label(self, text=group_name + self.time_string, font=LARGE_FONT, compound=CENTER,
                          fg='white', bg='black')
            code_label = Label(self, text="Insert 4 digit code: ", font=LARGE_FONT, compound=CENTER,
                               fg='white', bg='black')
            code_entry = Entry(self, show="*")
            code_button = ttk.Button(self, text="Enter", command=self.check_code)
            start_button, pause_button = self.create_music_buttons()
            group = Group(index, label, group_name, code_label, code_entry, code_button,
                          self.get_penalty(), start_button, pause_button)
            self.group_list.append(group)
        self.design_groups()
        self.start_button.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.pause_button.place(relx=0.4, rely=0.5, anchor=CENTER)

    def check_code(self):
        for group in self.group_list:
            if len(group.code_entry.get()) != 0:
                if group.check_code(group.code_entry.get()):
                    self.stop_game()
                    tkinter.messagebox.showinfo(title="Winner",
                                                message=f"{group.name} Won!\nTime: {group.time_string}")

    def stop_game(self):
        pygame.mixer.music.stop()
        self.stop_flag = True

    @staticmethod
    def play_music():
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

    def begin_game(self):
        self.play_music()
        self.stop_flag = False
        self.game()

    def game(self):
        if not self.stop_flag:
            for group in self.group_list:
                group.timer()
            self.after(1000, self.game)