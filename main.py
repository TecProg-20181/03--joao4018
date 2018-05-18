
from Classes.readWord import ReadWord
from Classes.game import Game
from Classes.player import Player

secretWord = ReadWord()
player = Player()
game = Game()

guesses = player.getGuesses()
secretWord.readWords()
secret = secretWord.reloadWord(guesses)
game.hangman(secret, guesses)
