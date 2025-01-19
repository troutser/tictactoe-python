from __future__ import annotations
import tkinter as tk
from tkinter import PhotoImage

class Vector2:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x}, {self.y})"
    def __add__(self, vec2: Vector2) -> Vector2:
        return Vector2(self.x + vec2.x, self.y + vec2.y)
    def __mul__(self, multiplier: float | Vector2) -> Vector2:
        if isinstance(multiplier, float):
            return Vector2(self.x * multiplier, self.y * multiplier)
        elif isinstance(multiplier, Vector2):
            return Vector2(self.x * multiplier.x, self.y * multiplier.y)
    def __truediv__(self, divisor: float) -> Vector2:
        return self*(1/divisor)
    def __sub__(self, vec2):
        return self + -1 * vec2
    def dot(self, vec2):
        return self.x * vec2.x + self.y * vec2.y

class RootObject:
    def __init__(self):
        self.root = tk.Tk()
        self.root.state("zoomed")

        self.canvas = tk.Canvas(
            self.root,
            width=self.root.winfo_screenwidth(),
            height=self.root.winfo_screenheight(),
            bg="black"
        )
        self.canvas.pack()
    def start(self):
        self.root.mainloop()

class TicTacToeCell:
    def __init__(self, rootObject: RootObject, position: Vector2, size: Vector2):
        self.tag = f"cell_{position.x}_{position.y}"
        self.rootObject = rootObject

        self.images = {
            'empty': PhotoImage(file="images/empty_cell.png"),
            'o': PhotoImage(file="images/o_cell.png"),
            'x': PhotoImage(file="images/x_cell.png")
        }
        self._state = "empty"

        self.UI_element = rootObject.canvas.create_image(
            position.x + size.x / 2, position.y + size.y / 2, image=self.images['empty'], tags=self.tag
        )

        rootObject.canvas.tag_bind(self.tag, "<Button-1>", self.on_left_click)
        rootObject.canvas.tag_bind(self.tag, "<Button-2>", self.on_middle_click)
        rootObject.canvas.tag_bind(self.tag, "<Button-3>", self.on_right_click)

    @property
    def state(self):
        return self._state
    @state.setter
    def state(self, value):
        if self._state == value:
            return 
        
        self._state = value
        self.update_image()

    def update_image(self):
        self.rootObject.canvas.itemconfig(self.UI_element, image=self.images[self.state])
    def on_left_click(self, event):
        self.state = 'x'
    def on_right_click(self, event):
        self.state = 'o'
    def on_middle_click(self, event):
        self.state = 'empty'