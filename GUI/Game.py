import pygame
import time
import tkinter.messagebox
from Utils.Utilities import resource_path
from Utils import ImageUtilities, Utilities
from Objects.Clock import Clock
from tkinter import *
from tkinter import ttk
from Objects.Group import Group
from itertools import cycle

LARGE_FONT = ("verdana", 20)
CLOCK_FONT = ("8514oem", 34, 'bold')


class Game(Frame):
    amount_of_groups = 1
    penalty = 300
    group_name_list = list()
    playlist = list()
    photo_path = None
    clock = Clock()

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        for r in range(self.winfo_screenwidth()):
            self.grid_rowconfigure(r, weight=1)
        for c in range(self.winfo_screenheight()):
            self.grid_columnconfigure(c, weight=1)

        self._count = self.clock.time_to_seconds()
        self.configure(background='black')
        self._time_string = time.strftime(self.clock.clock_to_str())
        pygame.mixer.init()
        self.stop_flag = False
        self.pause = False
        self.pause_count = 0
        self.load_music()
        self.add_to_playlist()
        self.playlist = cycle(self.playlist)
        self._group_list = list()
        self.start_button = ttk.Button(self, text="Start/Pause Game",
                                       command=self.begin_game)

        self.next_song_button = ttk.Button(self, text="Next Song",
                                           command=self.play_playlist)
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
    def load_music(song=resource_path("Music/DY.ogg")):
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
        amount_of_group = len(self.group_list)
        width_even = self.winfo_screenwidth() / amount_of_group
        width_odd = self.winfo_screenwidth() / (amount_of_group + 1)
        label_height = 20
        for index, group in enumerate(self.group_list):
            if self.photo_path:
                ImageUtilities.place_images(group, int(group.count // 120))
                if amount_of_group % 2 == 0:
                    group.canvas.create_window(width_even, label_height, anchor=CENTER, window=group.label)
                    group.canvas.create_window(width_even, label_height * 3, anchor=CENTER, window=group.code_entry)
                    group.canvas.create_window(width_even, label_height * 5, anchor=CENTER, window=group.code_button)
                    group.canvas.create_window(width_even, label_height * 7, anchor=CENTER, window=group.start_button)
                    group.canvas.create_window(0, label_height * 9, anchor=W, window=group.clue_buttons[0])
                    group.canvas.create_window(0, label_height * 11, anchor=W, window=group.clue_buttons[1])
                    group.canvas.create_window(0, label_height * 13, anchor=W, window=group.clue_buttons[2])
                else:
                    group.canvas.create_window(width_odd, label_height, anchor=CENTER, window=group.label)
                    group.canvas.create_window(width_odd, label_height * 3, anchor=CENTER, window=group.code_entry)
                    group.canvas.create_window(width_odd, label_height * 5, anchor=CENTER, window=group.code_button)
                    group.canvas.create_window(width_odd, label_height * 7, anchor=CENTER, window=group.start_button)
                    group.canvas.create_window(0, label_height * 9, anchor=W, window=group.clue_buttons[0])
                    group.canvas.create_window(0, label_height * 11, anchor=W, window=group.clue_buttons[1])
                    group.canvas.create_window(0, label_height * 13, anchor=W, window=group.clue_buttons[2])
            else:
                group.label.pack(padx=10, pady=10)
                group.time_label.pack(padx=10, pady=10)
                # group.code_label.pack()
                group.code_entry.pack(padx=5, pady=5)
                group.code_button.pack(padx=5, pady=5)
                group.start_button.pack(side=TOP, padx=10, pady=10)
                for button in group.clue_buttons:
                    button.pack(side=LEFT, padx=2, pady=2)

    @staticmethod
    def create_music_buttons(frame) -> Button:
        start_button = ttk.Button(frame, text="Play/Pause")
        return start_button

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

    def create_groups(self):
        group_amount = self.updated_amount()
        name_list = self.get_name_list()

        location_list = self.calculate_division(group_amount)
        for index, group_name in zip(range(1, group_amount + 1), name_list):
            tup = location_list[index-1]
            frame = Utilities.create_sub_frame(self, tup[0], tup[1], tup[2], tup[3])
            if (index + 1) % 2 != 0:
                canvas_row = tup[2] * 2
                canvas = Utilities.create_sub_canvas(frame, canvas_row, tup[3], 'black')
            else:
                canvas = Utilities.create_sub_canvas(frame, tup[2], tup[3], 'black')

            group_name = group_name + ": "
            group_name_label = Label(frame, text=group_name, font=CLOCK_FONT,
                                     fg='white', bg='black')
            time_label = Label(frame, text=self.time_string, font=CLOCK_FONT,
                               fg='white', bg='black')
            code_label = Label(frame, text="Insert 4 digit code: ", font=LARGE_FONT,
                               fg='white', bg='black')
            code_entry = Entry(frame, show="*", width=15, font=LARGE_FONT)
            code_button = ttk.Button(frame, text="Enter", command=self.check_code)
            start_button = self.create_music_buttons(frame)

            clue_buttons = Utilities.create_clue_button_list(frame)

            if self.photo_path:
                canvas = ImageUtilities.load_images(canvas, self.photo_path)
                canvas_width = int(canvas['width'])
                canvas_height = int(canvas['height'])
            else:
                canvas = None
                canvas_width = 0
                canvas_height = 0
            group = Group(index, group_name_label, time_label, group_name, code_label, code_entry, code_button,
                          start_button, canvas, canvas_width, canvas_height, self.clock, clue_buttons)
            self.group_list.append(group)

        self.start_button.grid(padx=10, pady=10)
        self.next_song_button.grid(row=self.start_button.grid_info()['row'],
                                   column=self.start_button.grid_info()['column']+1,
                                   padx=10, pady=10)
        self.design_groups()

    def check_code(self):
        for group in self.group_list:
            if len(group.code_entry.get()) != 0:
                if group.check_code(group.code_entry.get()):
                    self.stop_game()
                    tkinter.messagebox.showinfo(title="Winner",
                                                message=f"{group.name} Won!\nTime: {group.time_string}")

    def pause_music(self):
        if not self.stop_flag:
            pygame.mixer.music.pause()
            self.stop_flag = True

    # TODO: make pause and re-pause?
    def stop_game(self):
        pygame.mixer.music.stop()
        self.stop_flag = True

    @staticmethod
    def play_music(loop_flag=True):
        pygame.mixer.music.set_volume(0.5)
        if loop_flag:
            pygame.mixer.music.play(loops=-1)
        else:
            pygame.mixer.music.play()

    def play_playlist(self):
        try:
            next_song = next(self.playlist)
            self.load_music(next_song)
            self.play_music(loop_flag=False)
        except FileNotFoundError:
            print(f"Failed to find file... Can't play song")

    def begin_game(self):
        if not self.pause:
            self.pause = True
            if self.pause_count > 0:
                pygame.mixer.music.unpause()
            else:
                self.play_music()
            self.stop_flag = False
            self.game()
        else:
            self.pause = False
            self.pause_count += 1
            self.pause_music()

    def game(self):
        if not self.stop_flag:
            if not pygame.mixer.music.get_busy():
                self.play_playlist()
            for group in self.group_list:
                group.timer()
            self.after(1000, self.game)
