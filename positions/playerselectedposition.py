import pandas as pd


class PlayerSelectedPosition:

    def __init__(self, row, col, player):
        self.row = row
        self.col = col
        self.player = player

    def access_player(self) -> int:
        return self.player
