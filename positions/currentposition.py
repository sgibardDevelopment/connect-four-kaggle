import pandas as pd
from position import Position


class CurrentPosition(Position):

    def __init__(self, row, col):
        super().__init__(row, col)

    def evaluate_action_according_to_current_position(self, grid: pd.DataFrame, player: int) -> str:
        if self.__is_current_position_occupied_by_player(grid, player):
            return "increment"
        else:
            return "reinit"

    def __is_current_position_occupied_by_player(self, grid: pd.DataFrame, player: int) -> bool:
        return grid.iloc[self.row][self.col] == player
