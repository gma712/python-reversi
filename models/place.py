from enum import Enum


class Coordinate:
    def __init__(self, value: int):
        if value > 7 or value < 0:
            raise ValueError(
                f"The argument value must be between 0 and 7. But actual: {value}"
            )
        self.__value = value

    @staticmethod
    def from_string(input_value: str):
        if not isinstance(input_value, str):
            raise TypeError(
                f"The argument 'input_value' must be string. But actual: {type(input_value)}"
            )
        if not input_value.isdecimal():
            raise TypeError(
                "The argument 'input_value' must be convertible to int object."
            )
        return Coordinate(int(input_value))

    @property
    def value(self) -> int:
        return self.__value

    def __eq__(self, other):
        return self.value == other


class Coordinates:
    def __init__(self, x: Coordinate, y: Coordinate):
        self.__x = x
        self.__y = y

    @staticmethod
    def from_ints(x_int: int, y_int: int):
        return Coordinates(Coordinate(x_int), Coordinate(y_int))

    @property
    def x(self) -> Coordinate:
        return self.__x

    @property
    def y(self) -> Coordinate:
        return self.__y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class Stone(Enum):
    ENPTY = 0
    WHITE = 1
    BLACK = -1

    def __str__(self) -> str:
        return "Stone"


class Place:
    def __init__(self, coordinates: Coordinates, stone: Stone):
        self.__coordinates = coordinates
        self.__stone = stone

    @property
    def stone(self) -> int:
        return self.__stone.value

    @property
    def x(self) -> Coordinate:
        return self.__coordinates.x

    @property
    def y(self) -> Coordinate:
        return self.__coordinates.y

    def __repr__(self) -> str:
        return str(self.stone)

    def __str__(self) -> str:
        return "Place"

    @property
    def is_white(self) -> bool:
        return self.__stone is Stone.WHITE

    @property
    def is_black(self) -> bool:
        return self.__stone is Stone.BLACK

    @property
    def is_empty(self) -> bool:
        return self.__stone is Stone.ENPTY

    def set_stone(self, stone: Stone) -> None:
        self.__stone = stone

    def flip(self) -> None:
        self.__stone = Stone.BLACK if self.is_white else Stone.WHITE
