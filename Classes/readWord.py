import random
import string
from sets import Set
import sys
import logging

WORDLIST_FILENAME = "TextFile/words.txt"

class ReadWord():

    def __init__(self):
        logging.basicConfig(filename='log.log',level=logging.INFO)
        self.__logger = logging.getLogger(__name__)
        self.__inFile = ""
        self.__line = ""
        self.__wordlist = ""
        self.__secretword = ""
        self.__guessinger = ""
        self.__listwords = ""

    def loadingMessage(self):
        print "Loading word list from file..."        
        print "  ", len(self.__wordlist), "words loaded."

    def readWords(self):
        try:
            self.__inFile = open(WORDLIST_FILENAME, 'r', 0)
            self.__logger.info('Open file: %s', WORDLIST_FILENAME)

        except IOError as (errno, strerror):
            print "I/O error({0}): {1}".format(errno, strerror)
            self.__logger.error('File not found: %s', WORDLIST_FILENAME)
            sys.exit()
        self.__line = self.__inFile.readline()
        self.__wordlist = string.split(self.__line)
        self.__listwords = self.__wordlist


    def reloadWord(self, guesses):
        self.__secretword = random.choice(self.__listwords).lower()
        try:
            self.__guessinger = Set(list(self.__secretword))
            self.__logger.info('Success')
        except:
            print 'verify that the file is not wrong, corrupted, or has a reading problem'
            self.__logger.error('Problem with data received by file')
            sys.exit()           
        try:
            if len(self.__guessinger) > guesses:
                self.__logger.warn('insufficient guessinger: %d', len(self.__guessinger))
                self.__secretword = random.choice(self.__listwords).lower()
                return self.reloadWord(guesses)
        except RuntimeError:
            self.__logger.error('Delay in while')
            print 'it was not possible to find a word with the same or less '
            print 'quantity than your guesses'
            answer = raw_input('impossible to win wish to continue Y/N: ')
            if answer not in ['Y', 'y']:
                sys.exit()
        print 'There is '  , len(self.__guessinger), ' different letters'
        return self.__secretword
