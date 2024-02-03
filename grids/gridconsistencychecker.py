import pandas as pd


class GridConsistencyChecker:

    def __init__(self, rows, columns):
        self.__rows = rows
        self.__columns = columns

    def check_consistency(self):
        if self.__grid_size_is_too_small(self.__rows, self.__columns):
            raise (ValueError("Error : grid size is too small"))
        else:
            pass

    @staticmethod
    def __grid_size_is_too_small(rows, columns) -> bool:
        return rows < 2 or columns < 2

    @staticmethod
    def __create_empty_grid(rows, columns) -> pd.DataFrame:
        return pd.DataFrame(index=range(rows), columns=range(columns))
