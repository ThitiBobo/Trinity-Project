
class Board:

    DEFAULT_SCORE = 0
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
        pass

    def removePiece(self, player, x, y):
        pass

    def movePiece(self, old_x, old_y, new_x, new_y):
        pass

    def addDeadSpace(self, player):
        pass

    def incrementScore(self, player, val):
        pass

    def putDeadSpace(self, player, x, y):
        pass

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



