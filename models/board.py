from .place import Coordinates, Stone, Place


class Board:
    def __init__(self) -> None:
        self.__board = [
            [
                Place(
                    Coordinates.from_ints(i, j),
                    self.__first_stone(Coordinates.from_ints(i, j)),
                )
                for j in range(8)
            ]
            for i in range(8)
        ]

    def __str__(self) -> str:
        return "Board"

    def __first_stone(self, coordinates: Coordinates) -> Place:
        if coordinates == Coordinates(3, 3) or coordinates == Coordinates(4, 4):
            return Stone.WHITE
        if coordinates == Coordinates(3, 4) or coordinates == Coordinates(4, 3):
            return Stone.BLACK
        return Stone.ENPTY

    @property
    def values(self):
        return self.__board

    def place(self, coordinates: Coordinates) -> Place:
        return self.__board[coordinates.y.value][coordinates.x.value]

    def put(self, coordinates: Coordinates, stone: Stone):
        target_place = self.place(coordinates)
        if target_place.is_empty:
            target_place.set_stone(stone)
