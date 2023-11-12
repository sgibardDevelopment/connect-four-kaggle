class WinCounterCalculator:

    def __init__(self, win_counter: int, step=1):
        self.win_counter = win_counter
        self.step = step

    def apply_action(self, action: str) -> int:
        if action == "increment":
            self.__increment_win_counter()
        elif action == "reinit":
            self.__reinit_win_counter()
        else:
            self.__action_value_error()

        return self.__access_win_counter()

    def __increment_win_counter(self):
        self.win_counter += self.step

    def __reinit_win_counter(self):
        self.win_counter = 0

    def __action_value_error(self):
        raise (ValueError("Error : action can be either 'increment' or 'reinit'"))

    def __access_win_counter(self) -> int:
        return self.win_counter
