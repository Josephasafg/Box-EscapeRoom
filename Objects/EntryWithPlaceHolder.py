import tkinter as tk
from tkinter import StringVar
from tkinter import CENTER, NORMAL

LARGE_FONT = ("verdana", 20)


class EntryWithPlaceholder(tk.Entry):
    def __init__(self, master=None, placeholder="PLACEHOLDER", color='grey'):
        super().__init__(master, width=15, font=LARGE_FONT, justify=CENTER)
        self.code_entered = StringVar()
        self.code_entered.trace('w', self.limit_characters)
        self.placeholder = placeholder
        self.placeholder_color = color
        self.release_limit = StringVar()
        self.release_limit.trace('w', self.unlimit_characters)
        self.default_fg_color = self['fg']

        self.bind("<FocusIn>",  self.focus_in)
        self.bind("<FocusOut>", self.focus_out)

        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    def focus_in(self, *args):
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self.configure(show='*', textvariable=self.code_entered)
            self['fg'] = self.default_fg_color

    def focus_out(self, *args):
        if not self.get():
            self.configure(show='', textvariable=self.release_limit)
            self.put_placeholder()

    def limit_characters(self, *args):
        value = self.code_entered.get()
        if len(value) > 4:
            self.code_entered.set(value[:4])

    def unlimit_characters(self, *args):
        value = self.code_entered.get()
        if len(value) > 0:
            self.code_entered.set(value[:len(value)])
