import pandas as pd


class GridInitializer:

    def __init__(self, rows, columns):
        self.__rows = rows
        self.__columns = columns

    def init_grid(self) -> pd.DataFrame:
        return pd.DataFrame(data=0, index=range(self.__rows), columns=range(self.__columns))
