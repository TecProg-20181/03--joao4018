import random
import string
from sets import Set

WORDLIST_FILENAME = "TextFile/words.txt"
GUESSES = 8
class ReadWord():

    def __init__(self):
        self.inFile = ""
        self.line = ""
        self.wordlist = ""

    def loadingMessage(self):
        print "Loading word list from file..."        
        print "  ", len(self.wordlist), "words loaded."

    def readWords(self):
        self.inFile = open(WORDLIST_FILENAME, 'r', 0)
        self.line = self.inFile.readline()
        self.wordlist = string.split(self.line)
        return random.choice(self.wordlist)


    def reLoadWord(self,word, guesses):
        secretWord = word
        guessinger = Set(list(secretWord))
        while len(guessinger) > guesses:
            print 'There is ', len(guessinger),' different letters'
            print 'The word was', secretWord
            print 'Impossible to guess with', guesses, 'guesses'
            print 'We are looking for a new word. Wait a moment'
            print '---------------------------------------------'
            secretWord = self.readWords()
            guessinger = Set(list(secretWord))
        print 'There is '  , len(guessinger), ' different letters'
        return secretWord
