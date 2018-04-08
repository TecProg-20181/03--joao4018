
class Player():

    def __init__(self):
      self.__guesses = 8

    def getGuesses(self):
        return int(self.__guesses)

    def numberOfGuesses(self):
        print 'You can only play with words that have'
        print 'the same number of letter as or less than'
        print 'the number of guesses'
        while True:
            try:
                self.__guesses = int(raw_input('Choose the number of guesses to play: '))
                break
            except ValueError:
                print "Oops!  That was no valid number.  Try again..."
                print '----------------------------------------------'
        print 'Cool you have', self.__guesses, 'guesses'
