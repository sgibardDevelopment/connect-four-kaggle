import pandas as pd
from currentposition import CurrentPosition
from playerselectedposition import PlayerSelectedPosition
from enumgridmap import EnumGridMap


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
        elif self.check_type == "superior_positive_diagonal" or self.check_type == "inferior_positive_diagonal":
            return self.__is_current_position_on_a_border(current_position)
        else:
            self.__checker_value_error()

    def __is_current_position_on_a_border(self, current_position: CurrentPosition) -> bool:
        return current_position.row == 0 or current_position.col == 0 or current_position.row == self.nbr_rows - 1 or current_position.col == self.nbr_cols - 1

    def map_selected_position_type_of_place(self, player_selected_position: PlayerSelectedPosition) -> int:
        if player_selected_position.row == 0 and player_selected_position.col == 0:
            return EnumGridMap().high_left_corner
        elif player_selected_position.row == 0 and player_selected_position.col == self.nbr_cols - 1:
            return EnumGridMap().high_right_corner
        elif player_selected_position.row == self.nbr_rows - 1 and player_selected_position.col == 0:
            return EnumGridMap().low_left_corner
        elif player_selected_position.row == self.nbr_rows - 1 and player_selected_position.col == self.nbr_cols - 1:
            return EnumGridMap().low_right_corner
        elif player_selected_position.row == 0:
            return EnumGridMap().highest_row
        elif player_selected_position.row == self.nbr_rows - 1:
            return EnumGridMap().lowest_row
        elif player_selected_position.col == 0:
            return EnumGridMap().far_left_column
        elif player_selected_position.col == self.nbr_cols - 1:
            return EnumGridMap().far_right_column
        else:
            return EnumGridMap().not_a_border

    @staticmethod
    def __checker_value_error():
        raise (ValueError("Error : checker can be either horizontal or vertical or superior_positive_diagonal or inferior_negative_diagonal"))
