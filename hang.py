import random
import string

WORDLIST_FILENAME = "words.txt"

class readWord():

    def __init__(self):
        self.inFile = ""
        self.line = ""
        self.wordlist = ""

    def loadingMessage(self):
        print "Loading word list from file..."        
        print "  ", len(self.wordlist), "words loaded."

    def loadWords(self):
        self.inFile = open(WORDLIST_FILENAME, 'r', 0)
        self.line = self.inFile.readline()
        self.wordlist = string.split(self.line)
        return random.choice(self.wordlist)
        
class game():

    def __init__(self):
        self.lettersGuessed = ""

    def letrasDiferentes(self, secretWord):
        self.count = 0
        self.count2 = 0
        self.quantidade = 0
        while self.count < len(secretWord):
            self.letra = secretWord[0 + self.count]
            while self.count2 < len(secretWord) - 1:
                if self.letra == secretWord[1 + self.count2]:
                    self.quantidade += 1
                    self.count2 = len(secretWord)
                self.count2 += 1
            self.count += 1
            self.count2 = self.count
        print 'Existem'  , len(secretWord) - self.quantidade, 'letras diferentes'

    def isWordGuessed(self, secretWord):
    #    secretLetters = []

    #    for letter in secretWord:
    #        if letter in secretLetters:
    #            secretLetters.append(letter)
    #        else:
    #            pass

        for letter in secretWord:
            if letter in self.lettersGuessed:
                pass
            else:
                return False

        return True

    def getAvailableLetters(self):
        import string
        self.available = string.ascii_lowercase
        return self.available

    def lettersGuessedInWord(self, secretWord):
        self.guessed = ''
        for letter in secretWord:
            if letter in self.lettersGuessed:
                self.guessed += letter
            else:
                self.guessed += '_'
        return self.guessed

    def printWelcomeMessage(self, secretWord):
        print 'Welcome to the game, Hangam!'
        print 'I am thinking of a word that is', len(secretWord), ' letters long.'
        print '-------------'

    def hangman(self, secretWord):

        self.guesses = 8
        self.lettersGuessed = []

        while  self.isWordGuessed(secretWord) == False and self.guesses >0:
            print 'You have ', self.guesses, 'guesses left.'

            self.available = self.getAvailableLetters()
            for letter in self.available:
                if letter in self.lettersGuessed:
                    self.available = self.available.replace(letter, '')

            print 'Available letters', self.available
            letter = raw_input('Please guess a letter: ')
            if letter in self.lettersGuessed:
                self.guessed = self.lettersGuessedInWord(secretWord)

                print 'Oops! You have already guessed that letter: ', self.guessed
            elif letter in secretWord:
                self.lettersGuessed.append(letter)
                self.guessed = self.lettersGuessedInWord(secretWord)
                
                print 'Good Guess: ', self.guessed
            else:
                self.guesses -=1
                self.lettersGuessed.append(letter)
                self.guessed = self.lettersGuessedInWord(secretWord)

                print 'Oops! That letter is not in my word: ',  self.guessed
            print '------------'

        else:
            if self.isWordGuessed(secretWord) == True:
                print 'Congratulations, you won!'
            else:
                print 'Sorry, you ran out of guesses. The word was ', secretWord, '.'




secretWord = readWord()
jogo = game()

secret = secretWord.loadWords().lower()
secretWord.loadingMessage()

jogo.letrasDiferentes(secret)
jogo.printWelcomeMessage(secret)
jogo.hangman(secret)
