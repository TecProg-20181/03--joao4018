
from Classes.readWord import ReadWord
from Classes.game import Game
from Classes.player import Player

secretWord = ReadWord()
player = Player()
secret = secretWord.readWords().lower()

player.numberOfGuesses()
secretWord.reLoadWord(secret, player.getGuesses())
nada = player.getGuesses()
jogo = Game(secret, nada)
jogo.printWelcomeMessage()


jogo.hangman()
