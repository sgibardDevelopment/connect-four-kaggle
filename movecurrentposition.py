from currentposition import CurrentPosition


class MoveCurrentPosition:

    def __init__(self, current_position: CurrentPosition, step=1):
        self.current_position = current_position
        self.step = step

    def apply_movement(self, movement: str) -> CurrentPosition:
        if movement == "right":
            self.__move_current_position_to_the_right()
        elif movement == "below":
            self.__move_current_position_below()
        elif movement == "left":
            self.__move_current_position_to_the_left()
        elif movement == "above":
            self.__move_current_position_above()
        else:
            self.__movement_value_error()

        return self.__access_current_position()

    def __access_current_position(self) -> CurrentPosition:
        return self.current_position

    def __move_current_position_to_the_right(self):
        self.current_position.col += self.step

    def __move_current_position_below(self):
        self.current_position.row += self.step

    def __move_current_position_to_the_left(self):
        self.current_position.col -= self.step

    def __move_current_position_above(self):
        self.current_position.row -= self.step

    def __move_current_position_above_right(self):
        self.__move_current_position_above()
        self.__move_current_position_to_the_right()

    def __move_current_position_below_left(self):
        self.__move_current_position_below()
        self.__move_current_position_to_the_left()

    def __move_current_position_above_left(self):
        self.__move_current_position_above()
        self.__move_current_position_to_the_left()

    def __move_current_position_below_right(self):
        self.__move_current_position_below()
        self.__move_current_position_to_the_right()

    def __movement_value_error(self):
        raise (ValueError("Error : movement can be either 'right' or 'left' or 'below' or 'above'"))
