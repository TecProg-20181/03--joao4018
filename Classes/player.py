import warnings
class Player():

    def __init__(self):
      self.__guesses = 8

    def __numberOfGuesses(self):
        print 'You can only play with words that have'
        print 'the same number of letter or less than'
        print 'the number of guesses'
        while True:
            try:
                self.__guesses = int(raw_input('Choose the number of guesses to play: '))
                break
            except ValueError:
                print "Oops!  That was no valid number.  Try again..."
                print '----------------------------------------------'
        if(self.__guesses < 0):
            warnings.warn("number")
            return self.__numberOfGuesses()
        print 'Cool! You have', self.__guesses, 'guesses'

    def getGuesses(self):
        self.__numberOfGuesses()
        return self.__guesses