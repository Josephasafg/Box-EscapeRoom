import tkinter.messagebox
from tkinter import *
from tkinter import ttk
from PageOne import PageOne

LARGE_FONT = ("verdana", 14)


class StartPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.clock_amount_entry = Entry(self)
        self.show_main()

    def show_main(self):
        clock_amount_label = Label(self, text="Insert amount of clocks - ", font=LARGE_FONT)
        clock_amount_label.pack(pady=10, padx=10)

        self.clock_amount_entry.pack(pady=11, padx=11)
        button = ttk.Button(self, text="Enter",
                            command=lambda: self.check_clock_amount(self.clock_amount_entry.get()))

        # button = ttk.Button(self, text="Enter",
        #                     command=lambda: controller.show_frame(PageOne))
        button.pack()

    def check_clock_amount(self, amount):
        int_amount = int(amount)
        if int_amount > 4 or int_amount < 1:
            self.clock_amount_entry.delete("0", END)
            tkinter.messagebox.showwarning("Warning", "Input must be between 1-4")
        else:
            PageOne.amount_of_groups = int_amount
            self.controller.show_frame(PageOne)