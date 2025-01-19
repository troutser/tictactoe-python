import tkinter as tk
from modules.classes import PhysicsObject
from modules.classes import Vector2

ROOT_WIDTH, ROOT_HEIGHT = 1000, 500
RADIUS, STARTING_POSITION = 30, Vector2(500,0)

Root = tk.Tk()
Root.geometry(f"{ROOT_WIDTH}x{ROOT_HEIGHT}")

Canvas = tk.Canvas(
    Root,
    width=ROOT_WIDTH, 
    height=ROOT_HEIGHT,
    bg="white"
 )
Canvas.pack()

Circle = Canvas.create_oval(
    STARTING_POSITION.x, 
    STARTING_POSITION.y,
    RADIUS+STARTING_POSITION.x,
    RADIUS+STARTING_POSITION.y, 
    fill="blue"
)
Physics = PhysicsObject(
    position = STARTING_POSITION,
    velocity = Vector2(0,0),
    acceleration = Vector2(0,1)
)
def Step():
    Physics.step(0.01)
    if Physics.position.y > ROOT_HEIGHT - RADIUS:
        Physics.position.y = ROOT_HEIGHT * 2 - RADIUS * 2 - Physics.position.y
        Physics.velocity *= -1

    Canvas.coords(
        Circle, 
        Physics.position.x, 
        Physics.position.y,
        RADIUS+Physics.position.x, 
        RADIUS+Physics.position.y
    )
    print(Canvas.coords(Circle)[1])
    Root.after(30, Step)


Step()
Root.mainloop()