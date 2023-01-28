from .board import Board
from .place import Stone, Coordinates


class Player:
    def __init__(self, stone: Stone):
        self.__stone = stone

    def __str__(self) -> str:
        return "Player"

    @property
    def stone(self) -> Stone:
        return self.__stone

    def put(self, board: Board, coordinates: Coordinates):
        board.put(coordinates, self.stone)
