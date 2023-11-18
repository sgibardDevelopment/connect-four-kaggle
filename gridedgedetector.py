import pandas as pd
from currentposition import CurrentPosition


class GridEdgeDetector:

    def __init__(self, grid: pd.DataFrame, check_type: str):
        self.nbr_rows = grid.shape[0]
        self.nbr_cols = grid.shape[1]
        self.check_type = check_type

    def is_current_position_at_grid_edge(self, current_position: CurrentPosition) -> bool:
        if self.check_type == "horizontal":
            return current_position.col == self.nbr_cols - 1
        elif self.check_type == "vertical":
            return current_position.row == self.nbr_rows - 1
        else:
            self.__checker_value_error()

    @staticmethod
    def __checker_value_error():
        raise (ValueError("Error : checker can be either horizontal or vertical"))
