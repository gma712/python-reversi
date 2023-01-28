from models import Board, Player, Stone
from view import StandardIO


def main():
    view = StandardIO()
    board = Board()

    view.show_board(board)
    player = Player(Stone.BLACK)
    while True:
        player.put(board, view.get_coordinates())
        view.show_board(board)


if __name__ == '__main__':
    main()
