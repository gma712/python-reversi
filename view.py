from models import Board, Coordinate, Coordinates, Place


class StandardIO:
    def __init__(self):
        pass

    def show_board(self, board: Board):
        for row in board.values:
            print(*[self.__show_place(p) for p in row])

    def __show_place(self, place: Place):
        if place.is_white:
            return '●'
        if place.is_black:
            return '○'
        return '-'

    def __get_coordinate(self, message: str) -> Coordinate:
        input_value = input(f"{message}: ")
        return Coordinate.from_string(input_value)

    def get_coordinates(self) -> Coordinates:
        x = self.__get_coordinate("石を置く列を入力してください。(0 ~ 7)")
        y = self.__get_coordinate("石を置く行を入力してください。(0 ~ 7)")
        return Coordinates(x=x, y=y)
