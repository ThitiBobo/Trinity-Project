from src.game.Board import Board
from src.game.Game import Game
from src.game.player.Player import Player


class GameManager:

    def __init__(self, player1: Player, player2: Player):
        self.player1: Player = player1
        self.player2: Player = player2
        self.currentPlayer: Player = None

        self.board: Board = None
        self.game: Game = None

        self.gameFinished: bool = False

        self.init()

    def init(self):
        self.currentPlayer = self.player1
        self.board = Board()
        self.game = Game()
        self.gameFinished = False

    def changeCurrentPlayer(self):
        if self.currentPlayer == self.player1:
            self.currentPlayer = self.player2
        elif self.currentPlayer == self.player2:
            self.currentPlayer = self.player1
        else:
            raise Exception('error in changeCurrentPlayer()')

    def isGameFinished(self):
        pass

    def play(self):
        while not self.isGameFinished():
            self.currentPlayer.play()
            self.game.play()
            self.changeCurrentPlayer()
        self.endgame()

    def endgame(self):
        pass

    def stop(self):
        self.gameFinished = True


