import pandas as pd
from positions.playerselectedposition import PlayerSelectedPosition
from enumgridmap import EnumGridMap


class GridMapper:

    def __init__(self, grid: pd.DataFrame):
        self.nbr_rows = grid.shape[0]
        self.nbr_cols = grid.shape[1]

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
