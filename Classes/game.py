import string
import logging

class Game():

    def __init__(self):
        logging.basicConfig(filename='logFile.log',level=logging.INFO)
        self.__logger = logging.getLogger(__name__)
        self.__guesses = 8
        self.__secretWord = ""
        self.__letter = ""
        self.__lettersGuessed = ""
        self.__available = ""
        self.__guessed = ""
        
    def __isWordGuessed(self):
        for self.__letter in self.__secretWord:
            if self.__letter in self.__lettersGuessed:
                pass
            else:
                return False
        return True

    def __getAvailableLetters(self):
        self.__available = string.ascii_lowercase
        return self.__available

    def __lettersGuessedInWord(self):
        self.__logger.info('lettersGuessesInWord = passed')
        self.__guessed = ''
        for self.__letter in self.__secretWord:
            if self.__letter in self.__lettersGuessed:
                self.__guessed += self.__letter
            else:
                self.__guessed += '_'
        return self.__guessed

    def __printWelcomeMessage(self):
        print 'Welcome to the game, Hangam!'
        print 'I am thinking of a word that is', len(self.__secretWord), ' letters long.'
        print '-------------'

    def __removeChance(self):
        self.__logger.info('Loss chance')
        self.__guesses -=1
        self.__lettersGuessed.append(self.__letter)
        self.__guessed = self.__lettersGuessedInWord()
        print 'Oops! That letter is not in my word: ',  self.__guessed

    def __guessLetterInWord(self):
        self.__logger.info('Correct guess')
        self.__lettersGuessed.append(self.__letter)
        self.__guessed = self.__lettersGuessedInWord()      
        print 'Good Guess: ', self.__guessed
    
    def startHangmanGame(self,secretWord='abc', number=3):
        self.__logger.info('start Hangman Game')
        self.__guesses = number
        self.__secretWord = secretWord
        self.__lettersGuessed = []
        self.__printWelcomeMessage

        while  self.__isWordGuessed() == False and self.__guesses >0:
            print 'You have ', self.__guesses, 'guesses left.'
            self.__available = self.__getAvailableLetters()
            for self.__letter in self.__available:
                if self.__letter in self.__lettersGuessed:
                    self.__available = self.__available.replace(self.__letter, '')

            print 'Available letters', self.__available
            self.__letter = raw_input('Please guess a letter: ')
            self.__logger.info('letter inserted: %s', self.__letter)

            if self.__letter in self.__lettersGuessed:
                self.__guessed = self.__lettersGuessedInWord()
                print 'Oops! You have already guessed that letter: ', self.__guessed

            elif self.__letter in self.__secretWord:
                self.__guessLetterInWord()

            else:
                self.__removeChance()

            print '------------'

        else:
            if self.__isWordGuessed() == True:
                self.__logger.info('Finish game: Win')
                print 'Congratulations, you won!'
                
            else:
                print 'guessLorry, you ran out of guesses. The word was', self.__secretWord, '.'
                self.__logger.info('Finish game: Lose')
