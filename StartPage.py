import tkinter.messagebox
import os
from ImageUtilities import add_photo
from Utilities import create_sub_frame
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from GroupNamingPage import GroupNamingPage
from Clock import Clock
from Game import Game
from Group import Group

LARGE_FONT = ("verdana", 16)
MEDIUM_FONT = ("verdana", 10)


class StartPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        for r in range(self.winfo_screenwidth()):
            self.grid_rowconfigure(r, weight=1)
        for c in range(self.winfo_screenheight()):
            self.grid_columnconfigure(c, weight=1)
            
        self.configure(background='black')
        self.playlist = list()
        self._filename_path = None
        self.clock = Clock()
        self.clock_amount_entry = None
        self.hour_table = StringVar()
        self.minute_table = StringVar()
        self.playlist_frame = None
        self.playlist_box = None
        self.add_button = None
        self.delete_button= None
        self.photo_frame = None
        self.photo_button = None
        self.photo_entry = None
        self.password_frame = None
        self.password_entry = None
        self.code_entered = StringVar()
        self.code_entered.trace('w', self.limit_characters)
        self.show_main()

    @property
    def filename_path(self):
        return self._filename_path

    @filename_path.setter
    def filename_path(self, value):
        self._filename_path = value

    def create_photo_gui(self):
        photo_file_frame = create_sub_frame(self, 100, 2, 10, 10, "grey")
        self.photo_frame = Frame(photo_file_frame)
        self.photo_button = ttk.Button(self.photo_frame, text="Browse photos",
                                       command=lambda: add_photo(self.photo_entry))
        self.photo_entry = Entry(self.photo_frame)
        self.photo_frame.pack(side=LEFT, padx=30, pady=30)
        self.photo_entry.pack()
        self.photo_button.pack(side=LEFT)

    def create_duration_gui(self):
        outter_game_duration_label = create_sub_frame(self, 20, 40, 5, 5, 'black')
        # game_duration_label = Frame(outter_game_duration_label)
        # game_duration_label.pack(side=LEFT, padx=20, pady=20)
        game_duration_label = Label(outter_game_duration_label, text="Game Duration:", font=LARGE_FONT, fg='white', bg='black')

        game_duration_label.pack(pady=10, padx=10)

        outter_hour_frame = create_sub_frame(self, 30, 40, 5, 5, 'black')
        hour_frame = Frame(outter_hour_frame)
        hour_frame.pack(side=LEFT, padx=5, pady=5)
        hour_label = Label(hour_frame, text="Hours", font=MEDIUM_FONT, fg='black')
        hour_label.pack(side=LEFT, pady=5, padx=5)
        hour_box = ttk.Combobox(hour_frame, textvariable=self.hour_table, state='readonly',
                                values=['0', '1', '2'])
        hour_box.pack(side=LEFT, padx=5, pady=5)
        hour_box.current(1)

        outer_minute_frame = create_sub_frame(self, 35, 40, 5, 5, 'black')
        minute_frame = Frame(outer_minute_frame)
        minute_frame.pack(side=LEFT, padx=5, pady=5)
        minutes_label = Label(minute_frame, text="Minutes", font=MEDIUM_FONT, fg='black')
        minutes_label.pack(side=LEFT, pady=5, padx=5)
        minute_box = ttk.Combobox(minute_frame, textvariable=self.minute_table, state='readonly',
                                  values=Clock.get_minute_list())
        minute_box.pack(padx=5, pady=5)
        minute_box.current(0)

    def create_group_amount_gui(self):
        insert_amount_frame = create_sub_frame(self, 0, 0, 10, 10, "grey")
        clock_amount_label = Label(insert_amount_frame, text="Insert amount of groups: (1-6)", font=LARGE_FONT,
                                   fg='white', bg='black')
        self.clock_amount_entry = Entry(insert_amount_frame)
        enter_button = ttk.Button(insert_amount_frame, text="Enter",
                                  command=lambda: self.check_clock_amount(self.clock_amount_entry.get()))

        clock_amount_label.pack(padx=15, pady=15)
        self.clock_amount_entry.pack(pady=13, padx=13)
        enter_button.pack(padx=5, pady=5)

    def create_music_gui(self):
        music_frame = create_sub_frame(self, 100, 10, 10, 10, "grey")
        self.playlist_frame = Frame(music_frame)
        self.playlist_box = Listbox(self.playlist_frame)
        self.add_button = ttk.Button(self.playlist_frame, text="+ Add", command=self.browse_songs)
        self.delete_button = ttk.Button(self.playlist_frame, text="- Del", command=self.delete_song)
        self.playlist_frame.pack(side=LEFT, padx=30, pady=30)
        self.playlist_box.pack()
        self.add_button.pack(side=LEFT)
        self.delete_button.pack(side=LEFT)

    def create_password_gui(self):
        self.password_frame = create_sub_frame(self, 100, 40, 10, 10, "grey")
        password_label = Label(self.password_frame, text="Insert Password: ", font=LARGE_FONT,
                               fg='white', bg='black')
        self.password_entry = Entry(self.password_frame, textvariable=self.code_entered)
        password_label.pack()
        self.password_entry.pack()

    def show_main(self):
        self.create_group_amount_gui()
        self.create_photo_gui()
        self.create_music_gui()
        self.create_duration_gui()
        self.create_password_gui()

    def limit_characters(self, *args):
        value = self.code_entered.get()
        if len(value) > 4:
            self.code_entered.set(value[:4])

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
            Group.solving_password = self.password_entry.get()
            self.controller.add_class_to_tuple(GroupNamingPage)
            self.controller.show_frame(GroupNamingPage)