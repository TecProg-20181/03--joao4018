import logging
import warnings
class Player():

    def __init__(self):
        self.__guesses = 8
        logging.basicConfig(filename='logging.log',level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def __numberOfGuesses(self):
        print 'You can only play with words that have'
        print 'the same number of letter or less than'
        print 'the number of guesses'
        while True:
            try:
                self.__guesses = int(raw_input('Choose the number of guesses to play: '))
                self.logger.info('quantify guesses: %d', self.__guesses)
                break
            except ValueError:
                self.logger.error('Value entered is not number')
                print "Oops!  That was no valid number.  Try again..."
                print '----------------------------------------------'
        if(self.__guesses < 0):
            self.logger.warn('Value entered is number less than or equal to 0')
            print 'You entered that number ' + str(self.__guesses) + ' that is less than or equal to 0'
            print '----------------------------------------------'
            return self.__numberOfGuesses()
        print 'Cool! You have', self.__guesses, 'guesses'

    def getGuesses(self):
        self.__numberOfGuesses()
        return self.__guesses