import pandas as pd
from position import Position


class PlayerSelectedPosition(Position):

    def __init__(self, row, col, player):
        super().__init__(row, col)
        self.player = player

    def access_player(self) -> int:
        return self.player
