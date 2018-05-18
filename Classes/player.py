import logging
import warnings
import sys

class Player():

    def __init__(self):
        self.__guesses = 8
        logging.basicConfig(filename='log.log',level=logging.INFO)
        self.__logger = logging.getLogger(__name__)
        self.__logger.info('Hangman')
    def __printWelcome(self):
        print '------------------------------------------'
        print '|---------Welcome Hangman Game-----------|'
        print '| You can only play with words that have |'
        print '| the same number of letter or less than |'
        print '| the number of guesses                  |'
        print '------------------------------------------\n'

    def __numberOfGuesses(self):
        self.__printWelcome()
        while True:
            try:
                self.__guesses = int(raw_input('Choose the number of guesses to play: '))
                self.__logger.info('quantify guesses: %d', self.__guesses)
                break
            except ValueError:
                self.__logger.error('Value entered is not number')
                print "Oops!  That was no valid number.  Try again..."
                print '----------------------------------------------'
        if(self.__guesses < 0):
            self.__logger.warn('Value entered is number less than or equal to 0 number: %d', self.__guesses)
            print 'You entered that number ' + str(self.__guesses) + ' that is less than or equal to 0'
            print '----------------------------------------------'
            return self.__numberOfGuesses()
        print 'Cool! You have', self.__guesses, 'guesses\n'

    def getGuesses(self):
        self.__numberOfGuesses()
        if self.__guesses == None:
            print 'Problem found game will be terminated for security, restart'
            self.__logger.error('guesses = None')
            sys.exit()
        return self.__guesses