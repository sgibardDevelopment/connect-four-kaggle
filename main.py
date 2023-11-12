# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from kaggle_environments import make, evaluate
from boardgrid import BoardGrid
import pandas as pd

env = make("connectx", debug= True)

class Agent:

    def __init__(self, boardgrid: BoardGrid):
        self.boardgrid = boardgrid
        pass

board = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 2, 2,
         0, 0, 0, 0, 2, 1, 2, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 2, 1, 2, 0, 2, 0]
#print(len(board))
boardgrid = BoardGrid(rows=6, columns=7)

boardgrid.fill_grid(col=1, player=1)
print(boardgrid.grid)

boardgrid.fill_grid(col=1, player=1)
print(boardgrid.grid)

boardgrid.fill_grid(col=1, player=1)
print(boardgrid.grid)

boardgrid.fill_grid(col=1, player=1)
print(boardgrid.grid)

boardgrid.fill_grid(col=1, player=2)
print(boardgrid.grid)

boardgrid.fill_grid(col=1, player=2)
print(boardgrid.grid)

#print(list(env.agents))
#env.run(['random', 'random'])
#env.render(mode= "ipython")