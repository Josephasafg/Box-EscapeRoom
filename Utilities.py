from tkinter import Frame, Canvas, Button
from typing import List
from tkinter import W, E, N, S


def create_clue_button_list(frame: Frame) -> List[Button]:
    button_list = list()
    for button in range(1, 4):
        current_button = Button(frame, text=f"Clue #{button}")
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
