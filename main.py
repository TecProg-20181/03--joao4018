
from Classes.readWord import ReadWord
from Classes.game import Game
from Classes.player import Player

words = ReadWord()
player = Player()
hangmanGame = Game()

guesses = player.getGuesses()
words.readWords()
secretWord = words.loadWord(guesses)
hangmanGame.startHangmanGame(secretWord, guesses)
