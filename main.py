
from Classes.readWord import ReadWord
from Classes.game import Game
from Classes.player import Player

secretWord = ReadWord()
player = Player()
jogo = Game()

player.numberOfGuesses()

secret = secretWord.readWords().lower()
guesses = player.getGuesses()

secret = secretWord.reLoadWord(secret, guesses)
jogo.hangman(secret, guesses)
