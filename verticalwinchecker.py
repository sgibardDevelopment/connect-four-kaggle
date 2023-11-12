from winchecker import WinChecker
from currentposition import CurrentPosition


class VerticalWinChecker(WinChecker):

    def __init__(self, win_checker: WinChecker):
        super().__init__(win_checker.grid, win_checker.player_selected_position, win_checker.inarow)
        self.current_position = CurrentPosition(row=0, col=win_checker.player_selected_position.col)
        self.player = win_checker.player_selected_position.player

    def calculate_vertical_win_counter(self) -> int:
        return self._check_entire_lines(win_counter=0, current_position=self.current_position, check_type="vertical")
