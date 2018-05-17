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

    def loadingMessage(self):
        print "Loading word list from file..."        
        print "  ", len(self.__wordlist), "words loaded."

    def __readWords(self):
        try:
            self.__inFile = open(WORDLIST_FILENAME, 'r', 0)
            self.__logger.info('Open file')

        except IOError as (errno, strerror):
            print "I/O error({0}): {1}".format(errno, strerror)
            self.__logger.error('File not found')
            sys.exit()
        self.__line = self.__inFile.readline()
        self.__wordlist = string.split(self.__line)
        return random.choice(self.__wordlist)


    def reloadWord(self, guesses):
        self.__secretword = self.__readWords()
        try:
            self.__guessinger = Set(list(self.__secretword))
            self.__logger.info('Success')
        except:
            print 'verify that the file is not wrong, corrupted, or has a reading problem'
            self.__logger.error('Problem with data received by file')
            sys.exit()
        print 'There is ', len(self.__guessinger),' different letters'
        print 'The word was', self.__secretword
        print 'Impossible to guess with', guesses, 'guesses'
        print 'We are looking for a new word. Wait a moment'
        print '---------------------------------------------'
        if len(self.__guessinger) > guesses:
            self.__logger.warn('negative number entered')
            self.__secretword = self.__readWords().lower()
            return self.reloadWord(guesses)
        print 'There is '  , len(self.__guessinger), ' different letters'
        return self.__secretword
