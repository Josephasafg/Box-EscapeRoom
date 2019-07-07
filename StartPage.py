import tkinter.messagebox
from tkinter import *
from tkinter import ttk
from DropDown import DropDown
from Game import Game

LARGE_FONT = ("verdana", 16)
MEDIUM_FONT = ("verdana", 10)


class StartPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.configure(background='black')
        self.controller = controller
        self.clock_amount_entry = Entry(self)
        self.show_main()

    def show_main(self):
        clock_amount_label = Label(self, text="Insert amount of groups: (1-6)", font=LARGE_FONT, fg='white', bg='black')
        clock_amount_label.pack(pady=10, padx=10)

        self.clock_amount_entry.pack(pady=11, padx=11)
        button = ttk.Button(self, text="Enter",
                            command=lambda: self.check_clock_amount(self.clock_amount_entry.get()))

        # button = ttk.Button(self, text="Enter",
        #                     command=lambda: controller.show_frame(Game))
        button.pack()

    def check_clock_amount(self, amount):
        int_amount = int(amount)
        if int_amount > 6 or int_amount < 1:
            self.clock_amount_entry.delete("0", END)
            tkinter.messagebox.showwarning("Warning", "Input must be between 1-6")
        else:
            Game.amount_of_groups = int_amount
            self.controller.show_frame(DropDown)