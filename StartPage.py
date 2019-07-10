import tkinter.messagebox
import os
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from GroupNamingPage import GroupNamingPage
from Clock import Clock
from Game import Game

LARGE_FONT = ("verdana", 16)
MEDIUM_FONT = ("verdana", 10)


class StartPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.configure(background='black')
        self.playlist = list()
        self._filename_path = None
        self.clock = Clock()
        self.hour_table = StringVar()
        self.minute_table = StringVar()
        self.controller = controller
        self.clock_amount_entry = Entry(self)
        self.playlist_frame = Frame(self)
        self.photo_frame = Frame(self)
        self.photo_button = ttk.Button(self.photo_frame, text="Browse photos", command=self.add_photo)
        self.photo_entry = Entry(self.photo_frame)
        self.playlist_box = Listbox(self.playlist_frame)
        self.add_button = ttk.Button(self.playlist_frame, text="+ Add", command=self.browse_songs)
        self.delete_button = ttk.Button(self.playlist_frame, text="- Del", command=self.delete_song)
        self.show_main()

    def clock_frame(self):
        clock_frame = Frame(self)
        clock_frame.configure(background='black')
        clock_frame.pack(side=LEFT, padx=20, pady=20)
        game_duration_label = Label(clock_frame, text="Game Duration:", font=LARGE_FONT, fg='white', bg='black')
        hour_label = Label(clock_frame, text="Hours", font=MEDIUM_FONT, fg='white', bg='black')
        minutes_label = Label(clock_frame, text="Minutes", font=MEDIUM_FONT, fg='white', bg='black')
        game_duration_label.pack(pady=10, padx=10)
        hour_label.pack(side=LEFT, pady=5, padx=5)

        hour_box = ttk.Combobox(clock_frame, textvariable=self.hour_table, state='readonly',
                                values=['0', '1', '2'])
        hour_box.pack(side=LEFT, padx=5, pady=5)
        hour_box.current(1)
        minutes_label.pack(side=TOP, pady=5, padx=5)
        minute_box = ttk.Combobox(clock_frame, textvariable=self.minute_table, state='readonly',
                                  values=Clock.get_minute_list())
        minute_box.pack(padx=5, pady=5)
        minute_box.current(0)

    def add_photo(self):
        filename = filedialog.askopenfilename()
        self.photo_entry.insert(0, filename)

    @property
    def filename_path(self):
        return self._filename_path

    @filename_path.setter
    def filename_path(self, value):
        self._filename_path = value

    def show_main(self):
        middle_page = self.winfo_screenheight()
        clock_amount_label = Label(self, text="Insert amount of groups: (1-6)", font=LARGE_FONT, fg='white', bg='black')
        clock_amount_label.pack(padx=10, pady=10)
        self.clock_amount_entry.pack(pady=11, padx=11)
        button = ttk.Button(self, text="Enter",
                            command=lambda: self.check_clock_amount(self.clock_amount_entry.get()))
        button.pack()
        self.photo_frame.pack(padx=30, pady=30)

        self.playlist_frame.pack(side=LEFT, padx=30, pady=30)
        self.playlist_box.pack()
        self.add_button.pack(side=LEFT)
        self.delete_button.pack(side=LEFT)
        self.photo_entry.pack()
        self.photo_button.pack(side=LEFT)
        self.clock_frame()

    def browse_songs(self):
        self.filename_path = filedialog.askopenfilename()
        self.add_song_to_playlist()
        Game.playlist.append(self.filename_path)

    def add_song_to_playlist(self):
        filename = os.path.basename(self.filename_path)
        index = 0
        self.playlist_box.insert(index, filename)
        self.playlist.insert(index, self.filename_path)
        index += 1

    def delete_song(self):
        selected_song = int(self.playlist_box.curselection()[0])
        self.playlist_box.delete(selected_song)
        self.playlist.pop(selected_song)

    def check_clock_amount(self, amount):
        int_amount = int(amount)
        if int_amount > 6 or int_amount < 1:
            self.clock_amount_entry.delete("0", END)
            tkinter.messagebox.showwarning("Warning", "Input must be between 1-6")
        else:
            self.clock.parse_clock(self.hour_table.get(), self.minute_table.get())
            Game.clock.hour = self.clock.hour
            Game.clock.minute = self.clock.minute
            Game.amount_of_groups = int_amount
            Game.photo_path = self.photo_entry.get()
            self.controller.add_class_to_tuple(GroupNamingPage)
            self.controller.show_frame(GroupNamingPage)