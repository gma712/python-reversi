from models import Board
from view import StandardIO


def main():
    view = StandardIO()
    board = Board()

    view.show_board(board)


if __name__ == '__main__':
    main()
