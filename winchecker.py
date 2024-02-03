import pandas as pd
from positions.playerselectedposition import PlayerSelectedPosition
from positions.currentposition import CurrentPosition
from movecurrentposition import MoveCurrentPosition
from wincountercalculator import WinCounterCalculator
from gridedgedetector import GridEdgeDetector

class WinChecker:

    def __init__(self, grid: pd.DataFrame, player_selected_position: PlayerSelectedPosition, inarow:int):
        self.grid = grid
        self.player_selected_position = player_selected_position
        self.inarow = inarow

    def _check_entire_line(self, win_counter: int, current_position: CurrentPosition, check_type="horizontal") -> int:
        action = current_position.evaluate_action_according_to_current_position(self.grid, self.player_selected_position.access_player())
        win_counter = WinCounterCalculator(win_counter).apply_action(action)

        if self.__current_position_not_at_grid_edge(current_position, check_type):
            current_position = self.__move_to_next_position(win_counter, current_position, check_type)
            win_counter = self.__check_next_position(win_counter, current_position, check_type)
        else:
            # has reached a border or a player won the game
            pass

        return win_counter

    def __current_position_not_at_grid_edge(self, current_position, check_type):
        return not GridEdgeDetector(self.grid, check_type).is_current_position_at_grid_edge(current_position)

    def __check_next_position(self, win_counter: int, current_position: CurrentPosition, check_type: str):
        if self._game_is_won(win_counter):
            return win_counter
        else:
            return self._check_entire_line(win_counter, current_position, check_type)

    def __move_to_next_position(self, win_counter: int, current_position: CurrentPosition, check_type: str) -> CurrentPosition:
        if check_type == "horizontal":
            current_position = MoveCurrentPosition(current_position).apply_movement(movement="right")
        elif check_type == "vertical":
            current_position = MoveCurrentPosition(current_position).apply_movement(movement="below")
        else:
            self.__checker_value_error()

        return current_position

    def _game_is_won(self, win_counter: int) -> bool:
        return win_counter == self.inarow

    @staticmethod
    def __checker_value_error():
        raise (ValueError("Error : checker can be either horizontal or vertical"))