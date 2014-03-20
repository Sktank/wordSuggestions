__author__ = 'spencertank'
import sys
import re
import distance

from errors import raiseError
import parse

misspelledFileNotEnteredError = "Please specify a misspelled words file!"



def getSuggestedWords(word, wordFrequencies):
    suggestedWords = []
    print word
    for item in wordFrequencies:
        possibleWord = item[0]

        #quick check for possibility based on length
        if abs(len(word) - len(possibleWord)) > 2:
            continue

        #compute levenshtein distance
        editDistance = distance.levenshtein(word, possibleWord)
        if editDistance <= 2:
            suggestedWords.append(possibleWord)

    return suggestedWords

def formatSuggestion(word, suggestedWords):
    return "* " + word + ": " + str(suggestedWords) + "\n"

def suggestWords(misspelledWords, wordFrequencies, suggestionsFilename):

    #open suggestions file
    suggestions = open(suggestionsFilename, 'w')

    for word in misspelledWords:
        #find an array of the suggested words sorted by frequency
        suggestedWords = getSuggestedWords(word, wordFrequencies)
        suggestions.write(formatSuggestion(word, suggestedWords))


if __name__ == "__main__":
    try:
        misspelledFilename = str(sys.argv[1])
    except IndexError:
       raiseError(misspelledFileNotEnteredError)

    #try to read in the misspelled words file
    misspelledWords = parse.getMisspelledWords(misspelledFilename)

    wordFrequenciesFilename = "word_frequency.csv"
    #try to read in the word frequencies file
    wordFrequencies = parse.getWordFrequencies(wordFrequenciesFilename)

    suggestionsFilename = "suggestions.txt"

    suggestWords(misspelledWords, wordFrequencies, suggestionsFilename)
