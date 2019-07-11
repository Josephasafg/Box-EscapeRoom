from tkinter import Frame
from tkinter import W, E, N, S


def create_sub_frame(parent_frame, row, col, r_span, c_span, border_color="red") -> Frame:
    frame = Frame(parent_frame, highlightbackground=border_color, highlightcolor=border_color,
                  highlightthickness=2, bg='black')
    frame.grid(row=row, column=col, rowspan=r_span, columnspan=c_span, sticky=W + E + N + S)
    return frame
