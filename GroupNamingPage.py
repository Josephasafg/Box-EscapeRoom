import tkinter.messagebox
from tkinter import *
from tkinter import ttk
from Game import Game
from Group import Group

LARGE_FONT = ("verdana", 16)

class GroupNamingPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='black')
        self.amount_of_groups = Game.updated_amount()
        self.group_name_list_entry = list()
        self.group_name_list = list()
        self.create_group_boxes()
        next_button = ttk.Button(self, text="Next",
                                 command=self.get_all_names)
        next_button.pack()

    def create_group_boxes(self):
        for group in range(self.amount_of_groups):
            group_label = Label(self, text=f"Name of group number {group+1}: ",fg='white', bg='black', font=LARGE_FONT)
            group_name_entry = Entry(self)
            group_label.pack(fill=X)
            group_name_entry.pack()
            self.group_name_list_entry.append(group_name_entry)

    def get_all_names(self):
        for name in self.group_name_list_entry:
            self.group_name_list.append(name.get())

        Game.group_name_list = self.group_name_list
        self.controller.add_class_to_tuple(Game)
        self.controller.show_frame(Game)
