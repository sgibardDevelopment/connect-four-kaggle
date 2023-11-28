from gridbuilder import GridBuilder


class Grid:

    def __init__(self, rows=6, columns=7, inarow=4):
        self.rows = rows
        self.columns = columns
        self.inarow = inarow
        self.grid = GridBuilder(rows, columns).build()
        self.column_state = ["EMPTY"] * columns

