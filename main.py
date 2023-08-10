import numpy as np
import pygame
import sys
import math

PLAYER_ONE = 1
PLAYER_TWO = 2
ROW_COUNT = 6
COLUMN_COUNT = 7
SQUARE_SIZE = 100

pygame.init()

width = COLUMN_COUNT * SQUARE_SIZE
height = (ROW_COUNT + 1) * SQUARE_SIZE

size = (width, height)

screen = pygame.display.set_mode(size)
screen.fill((0, 0, 0))


def draw_board():
    for i in range(ROW_COUNT):
        for j in range(COLUMN_COUNT):
            pygame.draw.rect(screen, (0, 0, 200),
                             ((j * SQUARE_SIZE), i * SQUARE_SIZE + SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            pygame.draw.circle(screen, (0, 0, 0),
                               (int(j * SQUARE_SIZE + SQUARE_SIZE / 2),
                                int(i * SQUARE_SIZE + SQUARE_SIZE + SQUARE_SIZE / 2)), 45)


class ConnectFour:
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    is_won = False
    draw = False

    def __int__(self):
        pass

    def update_board(self):
        for i in range(ROW_COUNT):
            for j in range(COLUMN_COUNT):
                if self.board[i][j] == 1:
                    pygame.draw.circle(screen, (255, 255, 0),
                                       (int(j * SQUARE_SIZE + SQUARE_SIZE / 2),
                                        int(i * SQUARE_SIZE + SQUARE_SIZE + SQUARE_SIZE / 2)), 45)
                elif self.board[i][j] == 2:
                    pygame.draw.circle(screen, (200, 0, 0),
                                       (int(j * SQUARE_SIZE + SQUARE_SIZE / 2),
                                        int(i * SQUARE_SIZE + SQUARE_SIZE + SQUARE_SIZE / 2)), 45)
                pygame.display.update()

    # noinspection PyArgumentList
    def is_game_won(self, player_piece):
        # check vertical spaces
        for x in range(ROW_COUNT - 3):
            for y in range(COLUMN_COUNT):
                if self.board[x][y] == player_piece and self.board[x + 1][y] == player_piece and \
                        self.board[x + 2][y] == player_piece and \
                        self.board[x + 3][y] == player_piece:
                    self.is_won = True
                    return True

        # check horizontal spaces
        for x in range(ROW_COUNT):
            for y in range(COLUMN_COUNT - 3):
                if self.board[x][y] == player_piece and self.board[x][y + 1] == player_piece and \
                        self.board[x][y + 2] == player_piece and \
                        self.board[x][y + 3] == player_piece:
                    self.is_won = True
                    return True

        # check / diagonal spaces
        for x in range(ROW_COUNT - 3):
            for y in range(3, COLUMN_COUNT):
                if self.board[x][y] == player_piece and self.board[x + 1][y - 1] == player_piece and \
                        self.board[x + 2][y - 2] == player_piece and \
                        self.board[x + 3][y - 3] == player_piece:
                    self.is_won = True
                    return True

        # check \ diagonal spaces
        for x in range(ROW_COUNT - 3):
            for y in range(COLUMN_COUNT - 3):
                if self.board[x][y] == player_piece and self.board[x + 1][y + 1] == player_piece and self.board[x + 2][
                    y + 2] == player_piece and \
                        self.board[x + 3][y + 3] == player_piece:
                    self.is_won = True
                    return True

        return False

    def is_game_draw(self):
        self.draw = (not any(0 in sublist for sublist in self.board)) and not self.is_won

    def drop_piece(self, column, player):
        player_piece = 1 if player == 1 else 2
        for i in reversed(range(len(self.board))):
            if self.board[i][column] == 0:
                self.board[i][column] = player_piece
                self.update_board()
                self.is_game_won(player_piece)
                self.is_game_draw()
                break
        print(self.board)
        if self.is_won:
            print(f"Player {player_piece} wins!!")
        elif self.draw:
            print("Game ends in a draw")

    def is_valid_column(self, column):
        return self.board[0][column] == 0

    def get_next_open_row(self):
        pass


game = ConnectFour()

turn = 0

draw_board()
pygame.display.update()

while not game.is_won and not game.draw:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
        elif e.type == pygame.MOUSEBUTTONDOWN:
            position = e.pos
            col = math.floor(position[0] / SQUARE_SIZE)
            print(col)
            # Ask for player 1 input
            if turn == 0:
                # column = int(input("Player 1 make your selection(0-6): "))
                if game.is_valid_column(col):
                    game.drop_piece(col, PLAYER_ONE)
                turn = 1
            # Ask for player 2 input
            else:
                # column = int(input("Player 2 make your selection(0-6): "))
                if game.is_valid_column(col):
                    game.drop_piece(col, PLAYER_TWO)
                turn = 0
