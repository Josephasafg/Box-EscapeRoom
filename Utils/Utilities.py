import sys
import os
from tkinter import Frame, Canvas, Button
from typing import List
from tkinter import W, E, N, S


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def create_clue_button_list(frame: Frame) -> List[Button]:
    button_list = list()
    for button in range(1, 4):
        current_button = Button(frame, text=f"Clue #{button}", padx=3, pady=3, activebackground='red')
        button_list.append(current_button)
    return button_list


def create_sub_canvas(parent_frame: Frame, r_span: int, c_span: int, border_color="red") -> Canvas:
    canvas = Canvas(parent_frame, width=r_span, height=c_span, highlightbackground=border_color, highlightcolor=border_color,
                    highlightthickness=2, bg='black')
    # canvas.grid()
    return canvas


def create_sub_frame(parent_frame, row, col, r_span, c_span, border_color="red") -> Frame:
    frame = Frame(parent_frame, highlightbackground=border_color, highlightcolor=border_color,
                  highlightthickness=2, bg='black')
    frame.rowconfigure(0, weight=1)
    frame.columnconfigure(0, weight=1)
    frame.grid(row=row, column=col, rowspan=r_span, columnspan=c_span, sticky=W + E + N + S)
    return frame
