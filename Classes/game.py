import string

class Game():

    def __init__(self):
        self.guesses = 8
        self.secretWord = ""
        
    def __isWordGuessed(self):
        for letter in self.secretWord:
            if letter in self.lettersGuessed:
                pass
            else:
                return False

        return True

    def __getAvailableLetters(self):
        self.available = string.ascii_lowercase
        return self.available

    def __lettersGuessedInWord(self):
        self.guessed = ''
        for letter in self.secretWord:
            if letter in self.lettersGuessed:
                self.guessed += letter
            else:
                self.guessed += '_'
        return self.guessed

    def printWelcomeMessage(self):
        print 'Welcome to the game, Hangam!'
        print 'I am thinking of a word that is', len(self.secretWord), ' letters long.'
        print '-------------'

    def hangman(self,secretWord, number):


        self.guesses = number
        self.secretWord = secretWord
        self.lettersGuessed = []
        self.printWelcomeMessage

        while  self.__isWordGuessed() == False and self.guesses >0:
            print 'You have ', self.guesses, 'guesses left.'

            self.available = self.__getAvailableLetters()
            for letter in self.available:
                if letter in self.lettersGuessed:
                    self.available = self.available.replace(letter, '')

            print 'Available letters', self.available
            letter = raw_input('Please guess a letter: ')
            if letter in self.lettersGuessed:
                self.guessed = self.__lettersGuessedInWord()

                print 'Oops! You have already guessed that letter: ', self.guessed
            elif letter in self.secretWord:
                self.lettersGuessed.append(letter)
                self.guessed = self.__lettersGuessedInWord()
                
                print 'Good Guess: ', self.guessed
            else:
                self.guesses -=1
                self.lettersGuessed.append(letter)
                self.guessed = self.__lettersGuessedInWord()

                print 'Oops! That letter is not in my word: ',  self.guessed
            print '------------'

        else:
            if self.__isWordGuessed() == True:
                print 'Congratulations, you won!'
            else:
                print 'Sorry, you ran out of guesses. The word was', self.secretWord, '.'
