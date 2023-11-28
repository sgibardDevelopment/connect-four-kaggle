from positions.playerselectedposition import PlayerSelectedPosition
from winchecker import WinChecker
from horizontalwinchecker import HorizontalWinChecker
from verticalwinchecker import VerticalWinChecker
import pandas as pd


class BoardGrid:

    def __init__(self, rows=6, columns=7, inarow=4):
        self.rows = rows
        self.columns = columns
        self.inarow = inarow
        self.grid = self.__build_grid(rows, columns)
        self.column_state = ["EMPTY"] * columns

    def fill_grid(self, col: int, player: int):
        if self.__column_is_filled(col):
            self.__user_message_column_filled()
        else:
            player_selected_position = self.__check_for_free_position_in_column(self.grid, col, player)
            if self.__check_horizontal_win(HorizontalWinChecker(WinChecker(self.grid, player_selected_position, self.inarow)).calculate_horizontal_win_counter()):
                print("Endgame : horizontal")
            elif self.__check_vertical_win(VerticalWinChecker(WinChecker(self.grid, player_selected_position, self.inarow)).calculate_vertical_win_counter()):
                print("Endgame : vertical")

    def __column_is_filled(self, col) -> bool:
        return self.column_state[col] == "FILLED"

    @staticmethod
    def __user_message_column_filled():
        print("Column filled ! Try another one !")

    def __check_for_free_position_in_column(self, grid, col, player):
        for row in reversed(range(self.rows)):
            if self.__position_is_free(grid, row, col):
                return self.__play_in_column(grid, row, col, player)
            else:
                pass

    def __check_horizontal_win(self, horizontal_win_checker):
        #print('horizontal_win_checker =' + str(horizontal_win_checker))
        return horizontal_win_checker == self.inarow

    def __check_vertical_win(self, vertical_win_checker):
        #print('vertical_win_checker =' + str(vertical_win_checker))
        return vertical_win_checker == self.inarow

    @staticmethod
    def __position_is_free(grid, row, col) -> bool:
        return grid.iloc[row][col] == 0

    def __play_in_column(self, grid, row, col, player) -> PlayerSelectedPosition:
        if (row == 0) and (self.__position_is_free(grid, row=0, col=col)):
            self.column_state[col] = "FILLED"
        else:
            pass
        return self.__fill_column(row, col, player)

    def __fill_column(self, row, col, player) -> PlayerSelectedPosition:
        self.grid.iloc[row][col] = player
        return PlayerSelectedPosition(row, col, player)
