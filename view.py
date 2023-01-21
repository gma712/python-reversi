from models import Board, Place


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

