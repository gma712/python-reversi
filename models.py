from enum import Enum


class Board:
    def __init__(self, root: int = 8) -> None:
        self.root = root
        self.board = [[Coordinate(i, j) for j in range(self.root)] for i in range(self.root)]


class Color(Enum):
    LIGHT = 1
    DARK = 2


class Stone:
    def __init__(self, color: Color):
        self.color = color

    @staticmethod
    def light():
        return Stone(Color.LIGHT)

    @staticmethod
    def dark():
        return Stone(Color.DARK)

    @property
    def is_light(self) -> bool:
        return self.color is Color.LIGHT

    @property
    def is_dark(self) -> bool:
        return self.color is Color.DARK

    def flip(self) -> None:
        self.color = Color.DARK if self.is_light else Color.LIGHT


class Coordinate:
    def __init__(self, row: int, column: int):
        self.row = row
        self.column = column


class Player:
    def __init__(self, color: Color):
        self.color = color

    def put(self, coordinate: Coordinate):
        pass
