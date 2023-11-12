import pandas as pd


class CurrentPosition:

    def __init__(self, row, col):
        self.row = row
        self.col = col

    def evaluate_action_according_to_current_position(self, grid: pd.DataFrame, player: int) -> str:
        if self.__is_current_position_occupied_by_player(grid, player):
            return "increment"
        else:
            return "reinit"

    def __is_current_position_occupied_by_player(self, grid: pd.DataFrame, player: int) -> bool:
        return grid.iloc[self.row][self.col] == player
