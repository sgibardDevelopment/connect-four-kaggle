import pandas as pd
from gridconsistencychecker import GridConsistencyChecker
from gridinitializer import GridInitializer


class GridBuilder:

    def __init__(self, rows, columns):
        self.__rows = rows
        self.__columns = columns

    def build(self) -> pd.DataFrame:
        GridConsistencyChecker(self.__rows, self.__columns).check_consistency()
        return GridInitializer(self.__rows, self.__columns).init_grid()

