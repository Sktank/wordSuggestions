__author__ = 'spencertank'

from errors import raiseError
import re


frequenciesFormattingError = "Word frequencies formatting error on line: "
misspelledFormattingError = "Misspelled words formatting error on line: "
wordMatchRe = r"^[[a-zA-Z ]|\\]*$"


def frequenciesCheckIntegrity(frequencyList):
    wordRe = re.compile(wordMatchRe)
    for i, item in enumerate(frequencyList):
        #check that list is formatted correctly
        if not isinstance(item, list) or len(item) != 2:
            raiseError(frequenciesFormattingError + str(i))
        word = item[0]
        frequency = item[1]

        #check that first entry is a word
        if not wordRe.match(word):
            raiseError(frequenciesFormattingError + str(i))

        #check that second entry is an int
        try:
            int(frequency)
        except ValueError:
            raiseError(frequenciesFormattingError + str(i))

def misspelledCheckIntegrity(misspelledList):
    wordRe = re.compile(wordMatchRe)
    for i, word in enumerate(misspelledList):
        try:
            if not wordRe.match(word):
                raiseError(misspelledFormattingError + str(i))
        except TypeError:
            raiseError(misspelledFormattingError + str(i))