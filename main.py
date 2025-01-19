import tkinter as tk

class Vector2:
    def __init__(self, x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x}, {self.y})"
    def add(self, vec2):
        x = self.x + vec2.x
        y = self.y + vec2.y
    def mult(self, scalar):
        x = self.x * scalar
        y = self.y * scalar
    def div(self, divisor):
        self = self.mult(1/divisor)
    def sub(self, vec2):
        self = self.add(-vec2)

testVector = Vector2(3,1)
print(testVector.add(Vector2(1,2)))
