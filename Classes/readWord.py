import random
import string
from sets import Set
import sys

WORDLIST_FILENAME = "TextFile/words.txt"

class ReadWord():

    def __init__(self):
        self.__inFile = ""
        self.__line = ""
        self.__wordlist = ""


    def loadingMessage(self):
        print "Loading word list from file..."        
        print "  ", len(self.__wordlist), "words loaded."

    def readWords(self):
        try:
            self.__inFile = open(WORDLIST_FILENAME, 'r', 0)
        except IOError as (errno, strerror):
            print "I/O error({0}): {1}".format(errno, strerror)
            sys.exit()
        self.__line = self.__inFile.readline()
        self.__wordlist = string.split(self.__line)
        return random.choice(self.__wordlist)


    def reLoadWord(self,word, guesses):
        secretWord = word
        guessinger = Set(list(secretWord))
        while len(guessinger) > guesses:
            print 'There is ', len(guessinger),' different letters'
            print 'The word was', secretWord
            print 'Impossible to guess with', guesses, 'guesses'
            print 'We are looking for a new word. Wait a moment'
            print '---------------------------------------------'
            secretWord = self.readWords().lower()
            guessinger = Set(list(secretWord))
        print 'There is '  , len(guessinger), ' different letters'
        return secretWord
