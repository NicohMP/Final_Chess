import pygame
import sys
import numpy as np
from PIL import Image


def in_board(x, y):
    return x >= 0 and y >= 0 and x <= 7 and y <= 7


def case_empty(x, y, pieces):
    res = in_board(x, y)
    for piece in pieces.values():
        if (piece.x, piece.y) == (x, y):
            res = False
    return res


def ennemy_on_case(x, y, color_moving_piece, pieces):
    for piece in pieces.values():
        if (piece.x, piece.y) == (x, y):
            color_piece_encountered = piece.color
    return in_board(x, y) and color_moving_piece != color_piece_encountered


class Queen:
    def __init__(self, x, y, color) -> None:
        self.x = x
        self.y = y
        self.color = color

    def possible_moves(self, pieces):
        x, y = self.x + 1, self.y + 1
        possible_moves = []
        while case_empty(x, y, pieces):
            possible_moves.append([x, y])
            x += 1
            y += 1
        if ennemy_on_case(x, y, self.color, pieces):
            possible_moves.append((x, y))
        x, y = self.x + 1, self.y - 1
        while case_empty(x, y, pieces):
            possible_moves.append((x, y))
            x += 1
            y -= 1
        if ennemy_on_case(x, y, self.color, pieces):
            possible_moves.append((x, y))
        x, y = self.x - 1, self.y - 1
        while case_empty(x, y, pieces):
            possible_moves.append((x, y))
            x -= 1
            y -= 1
        if ennemy_on_case(x, y, self.color, pieces):
            possible_moves.append((x, y))
        if ennemy_on_case(x, y, self.color, pieces):
            possible_moves.append((x, y))
        x, y = self.x - 1, self.y + 1
        while case_empty(x, y, pieces):
            possible_moves.append((x, y))
            x -= 1
            y += 1
        if ennemy_on_case(x, y, self.color, pieces):
            possible_moves.append((x, y))
        x, y = self.x + 1, self.y
        while case_empty(x, y, pieces):
            possible_moves.append((x, y))
            x += 1
        if ennemy_on_case(x, y, self.color, pieces):
            possible_moves.append((x, y))
        x, y = self.x - 1, self.y
        while case_empty(x, y, pieces):
            possible_moves.append((x, y))
            x -= 1
        if ennemy_on_case(x, y, self.color, pieces):
            possible_moves.append((x, y))
        x, y = self.x, self.y + 1
        while case_empty(x, y, pieces):
            possible_moves.append((x, y))
            y += 1
        if ennemy_on_case(x, y, self.color, pieces):
            possible_moves.append((x, y))
        x, y = self.x, self.y - 1
        while case_empty(x, y, pieces):
            possible_moves.append((x, y))
            y -= 1
        if ennemy_on_case(x, y, self.color, pieces):
            possible_moves.append((x, y))
        return possible_moves


class Knigt:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def possible_moves(self, pieces):
        possible_moves = [
            [(self.x + 2, self.y - 1)],
            [(self.x + 2, self.y + 1)],
            [(self.x - 2, self.y - 1)],
            [(self.x - 2, self.y + 1)],
            [(self.x + 1, self.y + 2)],
            [(self.x - 1, self.y + 2)],
            [(self.x + 1, self.y - 2)],
            [(self.x - 1, self.y - 2)],
        ]
        for case in possible_moves:
            x, y = case[0], case[1]
            if not case_empty(x, y, pieces):
                possible_moves.remove(case)
        return possible_moves


class King:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def possible_moves(self, pieces):
        cases_possibles = [
            (self.x - 1, self.y - 1),
            (self.x, self.y - 1),
            (self.x + 1, self.y - 1),
            (self.x - 1, self.y),
            (self.x + 1, self.y),
            (self.x - 1, self.y + 1),
            (self.x, self.y + 1),
            (self.x + 1, self.y + 1),
        ]

        for case in cases_possibles:
            x, y = case[0], case[1]
            if not case_empty(x, y, pieces):
                cases_possibles.remove(case)

        return cases_possibles


class Rook:
    def __init__(self, x, y, color) -> None:
        self.x = x
        self.y = y
        self.color = color

    def possible_moves(self, pieces):
        x, y = self.x + 1, self.y
        possible_moves = []
        while case_empty(x, y, pieces):
            possible_moves.append((x, y))
            x += 1
        if ennemy_on_case(x, y, self.color, pieces):
            possible_moves.append((x, y))
        x, y = self.x - 1, self.y
        while case_empty(x, y, pieces):
            possible_moves.append((x, y))
            x -= 1
        if ennemy_on_case(x, y, self.color, pieces):
            possible_moves.append((x, y))
        x, y = self.x, self.y + 1
        while case_empty(x, y, pieces):
            possible_moves.append((x, y))
            y += 1
        if ennemy_on_case(x, y, self.color, pieces):
            possible_moves.append((x, y))
        x, y = self.x, self.y - 1
        while case_empty(x, y, pieces):
            possible_moves.append((x, y))
            y -= 1
        if ennemy_on_case(x, y, self.color, pieces):
            possible_moves.append((x, y))
        return possible_moves


class Bishop:
    def __init__(self, x, y, color) -> None:
        self.x = x
        self.y = y
        self.color = color

    def possible_moves(self, pieces):
        x, y = self.x + 1, self.y + 1
        possible_moves = []
        while case_empty(x, y, pieces):
            possible_moves.append([x, y])
            x += 1
            y += 1
        if ennemy_on_case(x, y, self.color, pieces):
            possible_moves.append((x, y))
        x, y = self.x + 1, self.y - 1
        while case_empty(x, y, pieces):
            possible_moves.append((x, y))
            x += 1
            y -= 1
        if ennemy_on_case(x, y, self.color, pieces):
            possible_moves.append((x, y))
        x, y = self.x - 1, self.y - 1
        while case_empty(x, y, pieces):
            possible_moves.append((x, y))
            x -= 1
            y -= 1
        if ennemy_on_case(x, y, self.color, pieces):
            possible_moves.append((x, y))
        if ennemy_on_case(x, y, self.color, pieces):
            possible_moves.append((x, y))
        x, y = self.x - 1, self.y + 1
        while case_empty(x, y, pieces):
            possible_moves.append((x, y))
            x -= 1
            y += 1
        if ennemy_on_case(x, y, self.color, pieces):
            possible_moves.append((x, y))
        return possible_moves


class BlackPawn:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = "black"

    def possible_moves(self, pieces):
        cases_possibles = [(self.x, self.y - 1), (self.x, self.y - 2)]
        for case in cases_possibles:
            x, y = case[0], case[1]
            if not case_empty(x, y, pieces):
                cases_possibles.remove(case)
        return cases_possibles


class WhitePawn:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = "white"

    def possible_moves(self, pieces):
        cases_possibles = [(self.x, self.y + 1), (self.x, self.y + 2)]
        for case in cases_possibles:
            if not case_empty(case, pieces):
                cases_possibles.remove(case)
        return cases_possibles


"""
class King_White:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def possible_mouvements(self):
        cases_possibles = [
            (self.x - 1, self.y - 1),
            (self.x, self.y - 1)[self.x] + 1,
            self.y - 1,
        ][self.x - 1, self.y][self.x + 1, self.y][self.x - 1, self.y + 1][
            self.x, self.y + 1
        ][
            self.position()[0] + 1, self.position()[1] + 1
        ]
        return cases_possibles
"""


class Board:
    def __init__(self) -> None:
        self.pieces = {
            "RW1": Rook(0, 0, "white"),
            "RW2": Rook(7, 0, "white"),
            "BW1": Bishop(2, 0, "white"),
            "BW2": Bishop(5, 0, "white"),
            "QW": Queen(3, 0, "white"),
            "PW1": WhitePawn(0, 1),
            "PW2": WhitePawn(1, 1),
            "PW3": WhitePawn(2, 1),
            "PW4": WhitePawn(3, 1),
            "PW5": WhitePawn(4, 1),
            "PW6": WhitePawn(5, 1),
            "PW7": WhitePawn(6, 1),
            "PW8": WhitePawn(7, 1),
            "PB1": BlackPawn(0, 6),
            "PB2": BlackPawn(1, 6),
            "PB3": BlackPawn(2, 6),
            "PB4": BlackPawn(3, 6),
            "PB5": BlackPawn(4, 5),
            "PB6": BlackPawn(5, 6),
            "PB7": BlackPawn(6, 6),
            "PB8": BlackPawn(7, 6),
            "RB1": Rook(0, 7, "black"),
            "RB2": Rook(7, 7, "black"),
            "BB1": Bishop(2, 7, "black"),
            "BB2": Bishop(5, 7, "black"),
            "QB": Queen(3, 7, "black"),
            "NB1": Knigt(1, 7, "black"),
            "NB2": Knigt(6, 7, "black"),
            "NW1": Knigt(1, 0, "white"),
            "NW2": Knigt(6, 0, "black"),
            "KW": King(4, 0, "white"),
            "KB": King(4, 7, "black"),
        }

    def possible_moves(self, piece):
        return piece.possible_moves(self.pieces)


board = Board()


def test_possibles_moves_for_pawn_A2():
    board = Board()

    pawn_A2 = board.pieces["PW1"]
    assert pawn_A2.y == 1
    assert pawn_A2.x == 0
    possible_moves_A1 = board.possible_moves(pawn_A2)
    assert possible_moves_A1 == [(0, 2)]
    pawn_B7 = board.pieces["PB2"]
    possible_moves_B7 = board.possible_moves(pawn_B7)
    # assert possible_moves_B7 == [(1, 5)]
    bishop_D3 = board.pieces["BW1"]
    possible_moves = board.possible_moves(bishop_D3)
    assert set(possible_moves) == set([(4, 4), (2, 2), (1, 1), (2, 4), (1, 5)])


board = Board()
rook_D3 = board.pieces["RW1"]
possible_moves = board.possible_moves(rook_D3)
print(possible_moves)


pygame.init()

clock = pygame.time.Clock()
table_size = 400
square_size = 50
screen = pygame.display.set_mode((table_size, table_size))
GRID_COLOR1 = (167, 103, 38)
GRID_COLOR2 = (245, 245, 220)


dico_im_address = {
    "PB": r"C:\Users\nhoubouyan\Desktop\cours\cours_info\Final_Chess\Chess_PB.png",
    "PW": r"C:\Users\nhoubouyan\Desktop\cours\cours_info\Final_Chess\Chess_PW.png",
    "NB": r"C:\Users\nhoubouyan\Desktop\cours\cours_info\Final_Chess\Chess_KnB.png",
    "NW": r"C:\Users\nhoubouyan\Desktop\cours\cours_info\Final_Chess\Chess_KnW.png",
    "BB": r"C:\Users\nhoubouyan\Desktop\cours\cours_info\Final_Chess\Chess_BB.png",
    "BW": r"C:\Users\nhoubouyan\Desktop\cours\cours_info\Final_Chess\Chess_BW.png",
    "RB": r"C:\Users\nhoubouyan\Desktop\cours\cours_info\Final_Chess\Chess_RB.png",
    "RW": r"C:\Users\nhoubouyan\Desktop\cours\cours_info\Final_Chess\Chess_RW.png",
    "QB": r"C:\Users\nhoubouyan\Desktop\cours\cours_info\Final_Chess\Chess_QB.png",
    "QW": r"C:\Users\nhoubouyan\Desktop\cours\cours_info\Final_Chess\Chess_QW.png",
    "KB": r"C:\Users\nhoubouyan\Desktop\cours\cours_info\Final_Chess\Chess_KB.png",
    "KW": r"C:\Users\nhoubouyan\Desktop\cours\cours_info\Final_Chess\Chess_KW.png",
}


def scaling(piece_im):
    height, width = square_size, square_size
    return pygame.transform.scale(piece_im, (height, width))


scaled_images = {}
for piece in dico_im_address.keys():
    scaled_images[piece] = pygame.image.load(dico_im_address[piece[:2]])
    scaled_images[piece] = scaling(scaled_images[piece])


def display_pieces(pieces):
    for piece_name in pieces.keys():
        image = pygame.image.load(dico_im_address[piece_name[:2]])
        scaled_image = scaling(image)
        piece = pieces[piece_name]
        screen.blit(scaled_image, (piece.x * square_size, (7 - piece.y) * square_size))


def display_moves(moves):
    for move in moves:
        x, y = move[0], move[1]
        pygame.draw.rect(
            screen,
            (0, 0, 255),
            (
                (x) * square_size,
                (7 - (y)) * square_size,
                square_size,
                square_size,
            ),
        )
    pygame.display.update()


PB1 = board.pieces["PB1"]
print(PB1.possible_moves(board.pieces))
display_moves(PB1.possible_moves(board.pieces))


running = True
screen.fill(GRID_COLOR2)
for i in range(0, table_size, square_size):
    for j in range(i, table_size + i, 2 * square_size):
        CASE = pygame.Rect(i, j % table_size, square_size, square_size)
        pygame.draw.rect(screen, GRID_COLOR1, CASE)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    display_pieces(board.pieces)
    BB2 = board.pieces["BB2"]
    display_moves(BB2.possible_moves(board.pieces))
    pygame.display.flip()

pygame.quit()
