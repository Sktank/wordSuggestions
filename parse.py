__author__ = 'spencertank'

from errors import raiseError
import verify

frequenciesFileNotFoundError = "The word frequencies file could not be found!"
misspelledFileNotFoundError = "The misspelled words file could not be found!"

def getWordFrequencies(frequenciesFilename):
    try:
        f = open(frequenciesFilename, 'r')
    except IOError:
        raiseError(frequenciesFileNotFoundError)

    frequencies = f.read()

    frequencyList = frequencies.split('\n')
    for i, item in enumerate(frequencyList):
        frequencyList[i] = item.split(',')

    verify.frequenciesCheckIntegrity(frequencyList)

    sorted(frequencyList, key=lambda item: int(item[1]))
    return frequencyList

def getMisspelledWords(misspelledFilename):
    #read in the input file
    try:
        f = open(misspelledFilename, 'r')
    except IOError:
        raiseError(misspelledFileNotFoundError)

    misspelled = f.read()
    misspelledWordsList = misspelled.split('\n')

    verify.misspelledCheckIntegrity(misspelledWordsList)

    return misspelledWordsList