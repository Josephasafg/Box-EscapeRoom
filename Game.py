import pygame
import time
import tkinter.messagebox
from typing import Tuple
from random import randint
from tkinter import *
from tkinter import ttk
from Group import Group
from itertools import cycle
from PIL import ImageTk, Image


LARGE_FONT = ("verdana", 20)


class Game(Frame):
    amount_of_groups = 1
    penalty = 300
    group_name_list = list()
    playlist = list()
    photo_path = None

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        for r in range(self.winfo_screenwidth()):
            self.grid_rowconfigure(r, weight=1)
        for c in range(self.winfo_screenheight()):
            self.grid_columnconfigure(c, weight=1)
        self._count = 3600
        self.configure(background='black')
        self._time_string = time.strftime("60:00:00")
        pygame.mixer.init()
        # self.group_name = "Group "
        self.stop_flag = False
        self.pause = False
        self.load_music()
        self.add_to_playlist()
        self.playlist = cycle(self.playlist)
        self._group_list = list()
        self.start_button = ttk.Button(self, text="Start/Pause Game",
                                       command=self.begin_game)
        self.create_groups()

    def add_to_playlist(self):
        for song in self.playlist:
            pygame.mixer.music.queue(song)

    @property
    def time_string(self):
        return self._time_string

    @time_string.setter
    def time_string(self, value):
        self._time_string = value

    @property
    def group_list(self):
        return self._group_list

    @group_list.setter
    def group_list(self, value):
        self._group_list = value

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value

    @staticmethod
    def load_music(song="Music/The Shortest Song_ An amazingly beautiful song by Bryant Oden.ogg"):
        try:
            pygame.mixer.music.load(song)
        except FileNotFoundError:
            print(f"Failed to find file {song}")

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
                group.label.pack(padx=10, pady=10)
                # group.code_label.pack()
                group.code_entry.pack(padx=5, pady=5)
                group.code_button.pack(padx=5, pady=5)
                group.start_button.pack(side=TOP, padx=10, pady=10)
            else:
                group.label.pack(padx=10, pady=30)
                # group.code_label.pack()
                group.code_entry.pack(padx=5, pady=5)
                group.code_button.pack(padx=5, pady=5)
                group.start_button.pack(side=TOP, padx=10, pady=10)
            if self.photo_path:
                self.place_images(group)

    @staticmethod
    def create_music_buttons(frame) -> Button:
        start_button = ttk.Button(frame, text="Play/Pause")
        return start_button

    def create_sub_frame(self, row, col, r_span, c_span) -> Frame:
        frame = Frame(self, highlightbackground='red', highlightcolor="red", highlightthickness=2, bg='black')
        frame.grid(row=row, column=col, rowspan=r_span, columnspan=c_span, sticky=W + E + N + S)
        return frame

    def calculate_division(self, index):
        locate_list = list()
        mid_w = self.winfo_screenwidth() // 2
        mid_h = self.winfo_screenheight() // 2
        tri_h = self.winfo_screenheight() // 3
        full_row = self.winfo_screenwidth()
        full_column = self.winfo_screenheight()
        if index == 2:
            locate1 = (0, 0, mid_w, full_column)
            locate2 = (mid_w, 0, mid_w, full_column)
            locate_list.append(locate1)
            locate_list.append(locate2)
        elif index == 3:
            locate1 = (0, 0, mid_w, mid_h)
            locate2 = (mid_w, 0, mid_w, mid_h)
            locate3 = (0, mid_h, full_row, mid_h)
            locate_list.append(locate1)
            locate_list.append(locate2)
            locate_list.append(locate3)
        elif index == 4:
            locate1 = (0, 0, mid_w, mid_h)
            locate2 = (mid_w, 0, mid_w, mid_h)
            locate3 = (0, mid_h, mid_w, mid_h)
            locate4 = (mid_w, mid_h, mid_w, mid_h)
            locate_list.append(locate1)
            locate_list.append(locate2)
            locate_list.append(locate3)
            locate_list.append(locate4)
        elif index == 5:
            locate1 = (0, 0, mid_w, tri_h)
            locate2 = (mid_w, 0, mid_w, tri_h)
            locate3 = (0, tri_h, mid_w, tri_h)
            locate4 = (mid_w, tri_h, mid_w, tri_h)
            locate5 = (0, full_column-tri_h, full_row, tri_h)
            locate_list.append(locate1)
            locate_list.append(locate2)
            locate_list.append(locate3)
            locate_list.append(locate4)
            locate_list.append(locate5)
        elif index == 6:
            locate1 = (0, 0, mid_w, tri_h)
            locate2 = (mid_w, 0, mid_w, tri_h)
            locate3 = (0, tri_h, mid_w, tri_h)
            locate4 = (mid_w, tri_h, mid_w, tri_h)
            locate5 = (0, full_column-tri_h, mid_w, tri_h)
            locate6 = (mid_w, full_column - tri_h, mid_w, tri_h)
            locate_list.append(locate1)
            locate_list.append(locate2)
            locate_list.append(locate3)
            locate_list.append(locate4)
            locate_list.append(locate5)
            locate_list.append(locate6)
        else:
            locate1 = (0, 0, full_row, full_column)
            locate_list.append(locate1)

        return locate_list

    @staticmethod
    def place_images(group):
        for image in range(10):
            rand_x = randint(0, group.width)
            rand_y = randint(0, group.height)
            group.image_list[image].place(x=rand_x, y=rand_y)

    def load_images(self):
        load = Image.open(self.photo_path)
        render = ImageTk.PhotoImage(load)
        return render

    @staticmethod
    def create_images(frame, rendered_image):
        image_list = list()
        for _ in range(10):
            img = Label(frame, image=rendered_image)
            img.image = rendered_image
            image_list.append(img)
        return image_list

    def create_groups(self):
        group_amount = self.updated_amount()
        name_list = self.get_name_list()

        location_list = self.calculate_division(group_amount)
        for index, group_name in zip(range(1, group_amount + 1), name_list):
            tup = location_list[index-1]
            frame = self.create_sub_frame(tup[0], tup[1], tup[2], tup[3])
            group_name = group_name + ": "
            label = Label(frame, text=group_name + self.time_string, font=LARGE_FONT,
                          fg='white', bg='black')
            code_label = Label(frame, text="Insert 4 digit code: ", font=LARGE_FONT,
                               fg='white', bg='black')
            code_entry = Entry(frame, show="*")
            code_button = ttk.Button(frame, text="Enter", command=self.check_code)
            start_button = self.create_music_buttons(frame)
            if self.photo_path:
                image = self.load_images()
                image_list = self.create_images(frame, image)
            else:
                image_list = None
            group = Group(index, label, group_name, code_label, code_entry, code_button,
                          self.get_penalty(), start_button, image_list, tup[2], tup[3])
            self.group_list.append(group)

        middle = self.winfo_screenwidth() // 2
        # self.start_button.pack(padx=10, pady=10)
        self.start_button.grid(padx=10, pady=10)
        self.design_groups()

    def check_code(self):
        for group in self.group_list:
            if len(group.code_entry.get()) != 0:
                if group.check_code(group.code_entry.get()):
                    self.stop_game()
                    tkinter.messagebox.showinfo(title="Winner",
                                                message=f"{group.name} Won!\nTime: {group.time_string}")

    # TODO: make pause and re-pause?
    def stop_game(self):
        pygame.mixer.music.stop()
        self.stop_flag = True

    @staticmethod
    def play_music():
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play()

    def begin_game(self):
        if not self.pause:
            self.pause = True
            self.play_music()
            self.stop_flag = False
            self.game()
        else:
            self.pause = False
            self.stop_game()

    def game(self):
        if not self.stop_flag:
            if not pygame.mixer.music.get_busy():
                next_song = next(self.playlist)
                self.load_music(next_song)
                self.play_music()
                # self.playlist.pop(next_song)
            for group in self.group_list:
                group.timer()
            self.after(1000, self.game)