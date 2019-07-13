import os
from Utils.ImageUtilities import add_photo
from Utils.Utilities import create_sub_frame
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from GUI.GroupNamingPage import GroupNamingPage
from Objects.Clock import Clock
from GUI.Game import Game
from Objects.Group import Group

LARGE_FONT = ("Book Antiqua", 18)
MEDIUM_FONT = ("verdana", 14)


class StartPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        for r in range(self.winfo_screenwidth()):
            self.grid_rowconfigure(r, weight=1)
        for c in range(self.winfo_screenheight()):
            self.grid_columnconfigure(c, weight=1)

        self.full_row = self.winfo_screenwidth()
        self.full_col = self.winfo_screenheight()
            
        self.configure(background='black')
        self.winfo_toplevel().title("MAX - IT'S A TOUGH WORLD.")
        self.playlist = list()
        self._filename_path = None
        self.clock = Clock()
        self.group_amount_entry = StringVar()
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
        x_label_frame = int(self.full_row // 5.0)
        y_label_frame = self.full_col // 4

        photo_file_frame = create_sub_frame(self, x_label_frame, y_label_frame, 10, 10, "black")
        self.photo_frame = Frame(photo_file_frame)
        photo_label = Label(self.photo_frame, text="Select a photo (optional):", font=LARGE_FONT,
                            fg='white', bg='black')
        self.photo_button = ttk.Button(self.photo_frame, text="Browse photos",
                                       command=lambda: add_photo(self.photo_entry))
        photo_label.pack()
        self.photo_entry = Entry(self.photo_frame)
        self.photo_frame.pack(side=LEFT, padx=30, pady=30)
        self.photo_entry.pack(side=RIGHT)
        self.photo_button.pack(side=LEFT)

    def create_duration_gui(self):
        x_label_frame = int(self.full_row // 6.0)
        y_label_frame = self.full_col // 2
        outter_game_duration_label = create_sub_frame(self, x_label_frame, y_label_frame, 5, 5, 'black')
        # game_duration_label = Frame(outter_game_duration_label)
        # game_duration_label.pack(side=LEFT, padx=20, pady=20)
        game_duration_label = Label(outter_game_duration_label, text="Game Duration:", font=LARGE_FONT, fg='white', bg='black')
        game_duration_label.pack(pady=10, padx=10)

        x_hour_frame = int(self.full_row // 5.9)
        y_hour_frame = self.full_col // 2
        outter_hour_frame = create_sub_frame(self, x_hour_frame, y_hour_frame, 5, 5, 'black')
        hour_frame = Frame(outter_hour_frame)
        hour_frame.pack(side=LEFT, padx=5, pady=5)
        hour_label = Label(hour_frame, text="Hours", font=MEDIUM_FONT, fg='black')
        hour_label.pack(side=LEFT, pady=5, padx=5)
        hour_box = ttk.Combobox(hour_frame, textvariable=self.hour_table, state='readonly',
                                values=['0', '1', '2'])
        hour_box.pack(side=LEFT, padx=5, pady=5)
        hour_box.current(1)

        x_minute_frame = int(self.full_row // 5.77)
        y_minute_frame = self.full_col // 2
        outer_minute_frame = create_sub_frame(self, x_minute_frame, y_minute_frame, 5, 5, 'black')
        minute_frame = Frame(outer_minute_frame)
        minute_frame.pack(side=LEFT, padx=5, pady=5)
        minutes_label = Label(minute_frame, text="Minutes", font=MEDIUM_FONT, fg='black')
        minutes_label.pack(side=LEFT, pady=5, padx=5)
        minute_box = ttk.Combobox(minute_frame, textvariable=self.minute_table, state='readonly',
                                  values=Clock.get_minute_list())
        minute_box.pack(padx=5, pady=5)
        minute_box.current(0)

    def create_group_amount_gui(self):
        x_frame = self.full_row // 6
        y_frame = self.full_col // 4
        options = ['1', '2', '3', '4', '5', '6']
        insert_amount_frame = create_sub_frame(self, x_frame, y_frame, 10, 10, "black")
        clock_amount_label = Label(insert_amount_frame, text="Insert amount of groups: (1-6)", font=LARGE_FONT,
                                   fg='white', bg='black')

        amount_box = ttk.Combobox(insert_amount_frame, textvariable=self.group_amount_entry, state="readonly",
                                  font=MEDIUM_FONT, values=options)
        clock_amount_label.pack(padx=15, pady=15)
        amount_box.pack(padx=10, pady=10)
        amount_box.current(0)

    def create_music_gui(self):
        x_label_frame = int(self.full_row // 2)
        y_label_frame = self.full_col // 4

        music_frame = create_sub_frame(self, x_label_frame, y_label_frame, 10, 10, "black")
        self.playlist_frame = Frame(music_frame)
        music_label = Label(self.playlist_frame, text="Add Music to playlist:", font=LARGE_FONT,
                            fg='white', bg='black')
        self.playlist_box = Listbox(self.playlist_frame)
        self.add_button = ttk.Button(self.playlist_frame, text="+ Add", command=self.browse_songs)
        self.delete_button = ttk.Button(self.playlist_frame, text="- Del", command=self.delete_song)
        music_label.pack(side=TOP)
        self.playlist_frame.pack(side=LEFT, padx=30, pady=30)
        self.playlist_box.pack()
        self.add_button.pack(side=LEFT)
        self.delete_button.pack(side=LEFT)

    def create_password_gui(self):
        x_frame = self.full_row // 6
        y_frame = int(self.full_col // 1.5)

        # x_frame = int(self.full_row // 3.5)
        # y_frame = self.full_col // 4
        self.password_frame = create_sub_frame(self, x_frame, y_frame, 10, 10, "black")
        password_label = Label(self.password_frame, text="Insert Password: ", font=LARGE_FONT,
                               fg='white', bg='black')
        self.password_entry = Entry(self.password_frame, textvariable=self.code_entered, font=MEDIUM_FONT)
        password_label.pack()
        self.password_entry.pack()

    def button_gui(self):
        enter_button = Button(self, text="Enter all parameters", font=('ariel', 14),
                              command=lambda: self.check_clock_amount(self.group_amount_entry.get()),
                              activebackground='red')
        enter_button.grid(column=int(self.full_col / 2), padx=10, pady=10, sticky=W)

    def show_main(self):
        self.create_group_amount_gui()
        self.create_duration_gui()
        self.create_password_gui()
        self.create_photo_gui()
        self.create_music_gui()
        self.button_gui()

    def limit_characters(self, *args):
        value = self.code_entered.get()
        if len(value) > 4:
            self.code_entered.set(value[:4])

    def browse_songs(self):
        self.filename_path = filedialog.askopenfilename()
        if self.filename_path != '':
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
        self.clock.parse_clock(self.hour_table.get(), self.minute_table.get())
        Game.clock.hour = self.clock.hour
        Game.clock.minute = self.clock.minute
        Game.amount_of_groups = int_amount
        Game.photo_path = self.photo_entry.get()
        if self.password_entry.get() != '':
            Group.solving_password = self.password_entry.get()
        self.controller.add_class_to_tuple(GroupNamingPage)
        self.controller.show_frame(GroupNamingPage)
