import numpy as np

PLAYER_ONE = 1
PLAYER_TWO = 2


class ConnectFour:
    ROW_COUNT = 6
    COLUMN_COUNT = 7
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))

    def __int__(self):
        pass

    def is_game_won(self, player_piece, current_row: int, current_col: int):
        for i in range(current_row - 1, current_row + 2):
            for j in range(current_col - 1, current_col + 2):
                if i in range(len(self.board)) and j in range(len(self.board[i])) and self.board[i][j] == player_piece:
                    print("hello", player_piece)
        pass

    def track_seeds(self, row, column, step):
        pass



    def drop_piece(self, column, player):
        player_piece = 1 if player == 1 else 2
        for i in reversed(range(len(self.board))):
            if self.board[i][column] == 0:
                self.board[i][column] = player_piece
                self.is_game_won(player_piece, i, column)
                break

        print(self.board)

    def is_valid_column(self, column):
        return self.board[0][column] == 0

    def get_next_open_row(self):
        pass


game = ConnectFour()

turn = 0

game_over = False

while not game_over:
    # Ask for player 1 input
    if turn == 0:
        col = int(input("Player 1 make your selection(0-6): "))
        if game.is_valid_column(col):
            game.drop_piece(col, PLAYER_ONE)
        turn = 1
    # Ask for player 2 input
    else:
        col = int(input("Player 2 make your selection(0-6): "))
        if game.is_valid_column(col):
            game.drop_piece(col, PLAYER_TWO)
        turn = 0
