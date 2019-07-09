import tkinter.messagebox
import os
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from DropDown import DropDown
from Game import Game

LARGE_FONT = ("verdana", 16)
MEDIUM_FONT = ("verdana", 10)


class StartPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.configure(background='black')
        self.playlist = list()
        self._filename_path = None
        self.controller = controller
        self.clock_amount_entry = Entry(self)
        left_frame = Frame(self)
        left_frame.pack(side=LEFT, padx=30, pady=30)
        self.playlist_box = Listbox(left_frame)
        self.add_button = ttk.Button(left_frame, text="+ Add", command=self.browse_songs)
        self.delete_button = ttk.Button(left_frame, text="- Del", command=self.delete_song)
        self.show_main()

    @property
    def filename_path(self):
        return self._filename_path

    @filename_path.setter
    def filename_path(self, value):
        self._filename_path = value

    def show_main(self):
        clock_amount_label = Label(self, text="Insert amount of groups: (1-6)", font=LARGE_FONT, fg='white', bg='black')
        clock_amount_label.pack(pady=10, padx=10)

        self.clock_amount_entry.pack(pady=11, padx=11)
        button = ttk.Button(self, text="Enter",
                            command=lambda: self.check_clock_amount(self.clock_amount_entry.get()))
        self.playlist_box.pack()
        self.add_button.pack(side=LEFT)
        self.delete_button.pack(side=LEFT)



        # button = ttk.Button(self, text="Enter",
        #                     command=lambda: controller.show_frame(Game))
        button.pack()

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
            Game.amount_of_groups = int_amount
            self.controller.show_frame(DropDown)