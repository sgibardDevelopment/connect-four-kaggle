from enumgridmap import EnumGridMap


class EnumDirection:

    def __init__(self):
        self.inferior_negative_diagonal = 0
        self.inferior_positive_diagonal = 1
        self.superior_positive_diagonal = 2
        self.superior_negative_diagonal = 3
        self.inferior_positive_and_negative_diagonals = 4
        self.superior_positive_and_negative_diagonals = 5
        self.superior_positive_and_inferior_negative_diagonals = 6
        self.inferior_positive_and_superior_negative_diagonals = 7
        self.direction_to_be_defined = 8

    def return_direction(self, grid_map_position: int) -> int:
        if grid_map_position == EnumGridMap().high_left_corner:
            return self.inferior_negative_diagonal
        elif grid_map_position == EnumGridMap().high_right_corner:
            return self.inferior_positive_diagonal
        elif grid_map_position == EnumGridMap().low_left_corner:
            return self.superior_positive_diagonal
        elif grid_map_position == EnumGridMap().low_right_corner:
            return self.superior_negative_diagonal
        elif grid_map_position == EnumGridMap().highest_row:
            return self.inferior_positive_and_negative_diagonals
        elif grid_map_position == EnumGridMap().lowest_row:
            return self.superior_positive_and_negative_diagonals
        elif grid_map_position == EnumGridMap().far_left_column:
            return self.superior_positive_and_inferior_negative_diagonals
        elif grid_map_position == EnumGridMap().far_right_column:
            return self.inferior_positive_and_superior_negative_diagonals
        elif grid_map_position == EnumGridMap().not_a_border:
            return self.direction_to_be_defined
