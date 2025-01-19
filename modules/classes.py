from __future__ import annotations
import math as math

class Vector2:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x}, {self.y})"
    def __add__(self, vec2: Vector2) -> Vector2:
        self.x = self.x + vec2.x
        self.y = self.y + vec2.y

        return self
    def __mul__(self, scalar: float) -> Vector2:
        self.x = self.x * scalar
        self.y = self.y * scalar

        return self
    def __truediv__(self, divisor: float) -> Vector2:
        self = self*(1/divisor)

        return self
    def __sub__(self, vec2):
        self = self + -1 * vec2

        return self
    def dot(self, vec2):
        return self.x * vec2.x + self.y * vec2.y
    
class PhysicsObject:
    def __init__(self, position: Vector2, velocity: Vector2, acceleration: Vector2):
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration
    def step(self, dt: float) -> PhysicsObject:
        self.position += self.velocity
        self.velocity += self.acceleration
        
        return self