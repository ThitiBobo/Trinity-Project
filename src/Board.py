from src.errors.IllegalActionError import IllegalActionError
from src.errors.IllegalArgumentError import IllegalArgumentError

'''
    Class Board
'''


class Board:
    DEFAULT_SCORE = 0
    DEFAULT_SCORE_TO_WIN = 3
    DEFAULT_NB_PIECE = 5
    DEFAULT_NB_DEAD_SPACE = 4
    DEFAULT_NB_DEAD_SPACE_BY_PLAYER = 0

    EMPTY_CELL_VALUE = 0
    P1_PIECE_CELL_VALUE = 1
    P2_PIECE_CELL_VALUE = 2
    DEAD_CELL_VALUE = 3

    def __init__(self):
        self.board = [0] * (5 * 5)
        self.initBoard()

        self.nbPieceP1: int = self.DEFAULT_NB_PIECE
        self.nbPieceP2: int = self.DEFAULT_NB_PIECE
        self.nbDeadSpace: int = self.DEFAULT_NB_DEAD_SPACE
        self.nbDeadSpaceP1: int = self.DEFAULT_NB_DEAD_SPACE_BY_PLAYER
        self.nbDeadSpaceP2: int = self.DEFAULT_NB_DEAD_SPACE_BY_PLAYER
        self.scoreP1: int = self.DEFAULT_SCORE
        self.scoreP2: int = self.DEFAULT_SCORE

    def initBoard(self):
        n = 5
        val_x = [0, 0, 1, n - 1, n - 1, n - 2]
        val_y = [0, 1, 0, n - 1, n - 2, n - 1]
        for i in range(len(val_x)):
            self.board[5 * val_x[i] + val_y[i]] = Board.DEAD_CELL_VALUE

    def putPiece(self, player, x, y):
        if self.board[5 * x + y] != Board.EMPTY_CELL_VALUE:
            raise IllegalActionError('putPiece')
        if player != Board.P1_PIECE_CELL_VALUE and player != Board.P2_PIECE_CELL_VALUE:
            raise IllegalArgumentError('player does not exist')
        self.board[5 * x + y] = player

    def removePiece(self, x, y):
        if self.board[5 * x + y] != Board.P1_PIECE_CELL_VALUE or \
                self.board[5 * x + y] != Board.P2_PIECE_CELL_VALUE:
            raise IllegalActionError('removePiece')
        self.board[5 * x + y] = Board.EMPTY_CELL_VALUE

    def movePiece(self, old_x, old_y, new_x, new_y):
        if self.board[5 * old_x + old_y] == Board.EMPTY_CELL_VALUE or \
                self.board[5 * new_x + new_y] != Board.EMPTY_CELL_VALUE:
            raise IllegalActionError('movePiece')
        self.board[5 * new_x + new_y] = self.board[5 * old_x + old_y]
        self.board[5 * old_x + old_y] = Board.EMPTY_CELL_VALUE

    def addDeadSpace(self, player):
        if self.nbDeadSpace == 0:
            raise IllegalActionError('addDeadSpace", "no dead space remaining')
        if player == Board.P1_PIECE_CELL_VALUE:
            self.nbDeadSpaceP1 += 1
        elif player == Board.P2_PIECE_CELL_VALUE:
            self.nbDeadSpaceP2 += 1
        else:
            raise IllegalArgumentError('player does not exist')

    def incrementScore(self, player, val):
        if val <= 0:
            raise IllegalArgumentError('score must have a positive value')
        if player == Board.P1_PIECE_CELL_VALUE:
            self.scoreP1 += val
        elif player == Board.P2_PIECE_CELL_VALUE:
            self.scoreP2 += val
        else:
            raise IllegalArgumentError('player does not exist')

    def putDeadSpace(self, player, x, y):
        if self.board[5 * x + y] != Board.EMPTY_CELL_VALUE:
            raise IllegalActionError('putDeadSpace')
        if player != Board.P1_PIECE_CELL_VALUE and player != Board.P2_PIECE_CELL_VALUE:
            raise IllegalArgumentError('player does not exist')
        self.board[5 * x + y] = Board.DEAD_CELL_VALUE

    def isFinished(self):
        if self.scoreP1 >= Board.DEFAULT_SCORE_TO_WIN:
            return Board.P1_PIECE_CELL_VALUE
        elif self.scoreP2 >= Board.DEFAULT_SCORE_TO_WIN:
            return Board.P2_PIECE_CELL_VALUE
        else:
            return 0

    def _toStringBoard(self):
        return ''.join(
            "[  {}] \r\n".format(
                ''.join(
                    "{}  ".format(self.board[5 * i + j])
                    for j in range(5)
                )
            )
            for i in range(5)
        )

    def __str__(self):
        string = ''
        string = string.__add__(self._toStringBoard() + '\r\n')
        string = string.__add__('score P1 : ' + self.scoreP1.__str__() + '\r\n')
        string = string.__add__('score P2 : ' + self.scoreP2.__str__() + '\r\n')
        string = string.__add__('\r\n')
        string = string.__add__('nb dead space    : ' + self.nbDeadSpace.__str__() + '\r\n')
        string = string.__add__('nb dead space p1 : ' + self.nbDeadSpaceP1.__str__() + '\r\n')
        string = string.__add__('nb dead space p2 : ' + self.nbDeadSpaceP2.__str__() + '\r\n')
        string = string.__add__('nb piece p1 : ' + self.nbPieceP1.__str__() + '\r\n')
        string = string.__add__('nb piece p2 : ' + self.nbPieceP2.__str__() + '\r\n')
        return string
