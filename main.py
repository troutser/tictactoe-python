from modules.classes import RootObject
from modules.classes import TicTacToeCell
from modules.classes import Vector2

PADDING, GRID_SIZE, CELL_SIZE = Vector2(10,10), Vector2(3,3), Vector2(100,100)

rootObject = RootObject()
cells = []
for x in range(GRID_SIZE.x):
    for y in range(GRID_SIZE.y):
        grid_position = Vector2(x,y)
        screen_position = grid_position * CELL_SIZE
        padding = PADDING * grid_position 
        cells.append(TicTacToeCell(
            rootObject,
            screen_position + padding,
            CELL_SIZE,
        ))

rootObject.start()