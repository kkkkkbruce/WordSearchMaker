#-------------------------------------------------------------------------------
# Name:        WordSearchMaker
# Purpose:     Create a simple text based word search for kids in any language
#              I'm sure I borrowed code from someone and adapted it, but I have
#              long since forgotten from whom, so please let me know if it was
#              you.
#
# Author:      Kevin
#
# Created:     25/04/2018
# Copyright:   (c) Kevin 2018
# Licence:    The MIT License (MIT)
#-------------------------------------------------------------------------------
import random
import os

all_letters_filename = 'AwaBibleLetters.txt'
word_list_filename = 'WordSearch.txt'

script_dir = os.path.dirname(__file__)
LettersFilePath = os.path.join(script_dir, all_letters_filename)
WordListPath = os.path.join(script_dir, word_list_filename)

#get letters list from file (some languages have different letters in their alphabet)
letters = []
with open(LettersFilePath, "r", encoding='utf-8') as LetterFile:
    for letter in LetterFile:
        if letter[0].upper() not in letters:
            letters.append(letter[0].upper())
#get word list from file
wordlist = []
with open(WordListPath, "r", encoding='utf-8') as WordFile:
    for word in WordFile:
        if word.strip() not in wordlist:
            wordlist.append(word.strip())
            
#text for printing data
direction = ["across","down"]
#set width and height
w, h = 20, 20
#create blank matrix with underscores as place holders
WS = [['_'] * w for i in range(h)]

def PrintMatrix(Matrix):
    for row in Matrix:
        columnString = ""
        for item in row:
            columnString += (str(item) + " ")
        print(columnString)




def main():
    #cycle through sorted word list (longest first)
    for word in sorted(wordlist, key=str.__len__, reverse=True):
##        print("\n")
##        print(word)
        fits = False
        empty = False
        tries = 0
        #pick a random spot/direction and see if word fits
        while fits == False or empty == False:
            #pick random spot, direction
            RandX = random.randint(0,h-1)
            RandY = random.randint(0,w-1)
            RandDir = random.randint(0,1) #across or down
##            print("Trying ({},{}) {}".format(RandX,RandY,direction[RandDir]))

            if RandDir==0: #across
                if RandY + len(word) <= w:
                    fits = True
##                    print("It Fits!")
##                else:
##                    print("doesn't fit, Max Y is {} and it would go to {}".format(w,RandY + len(word)))

            if RandDir==1: #down
                if RandX + len(word) <= h:
                    fits = True
##                    print("It Fits!")
##                else:
##                    print("doesn't fit, Max X is {} and it would go to {}".format(h,RandX + len(word)))

            if fits==True:
                #see if space empty or compatible letter is along the way
                if RandDir==0: #across
##                    print("Checking for empty or compatible letters across in matrix")
                    empty = True
                    l = 0
                    while (empty == True) and (l < len(word)):
                        if not(WS[RandX][RandY+l] == "_" or WS[RandX][RandY+l] == word[l]):
                            empty = False
                            fits = False
##                            print("OOPS! ({}, {}) is filled with {}".format(RandX,RandY+l, WS[RandX][RandY+l]))
##                            print("get new X & Y")
##                        else:
##                            print("({}, {}) is OK".format(RandX,RandY+l))
                        l+=1

                if RandDir==1: #down
##                    print("Checking for empty or compatible letters down in matrix")
                    empty = True
                    l = 0
                    while (empty == True) and (l < len(word)):
                       if not(WS[RandX+l][RandY] == "_" or WS[RandX+l][RandY] == word[l]):
                            empty = False
                            fits = False
##                            print("OOPS! ({}, {}) is filled with {}".format(RandX+l,RandY, WS[RandX+l][RandY]))
##                            print("get new X & Y")
##                       else:
##                            print("({}, {}) is OK".format(RandX+l,RandY))
                       l+=1
        #place word
##        print("Placing {} at ({},{}) {}".format(word,RandX,RandY,direction[RandDir]))
        if RandDir==0: #across
            for l in range(len(word)):
                WS[RandX][RandY+l]=word[l]
        if RandDir==1: #down
            for l in range(len(word)):
                WS[RandX+l][RandY]=word[l]



##    print()
##    print(wordlist)
    for word in wordlist:
        print(word)
    print()

    PrintMatrix(WS)

    #fill matrix with random letters
    for x in range(len(WS)):
        for y in range(len(WS[x])):
            if WS[x][y] == '_':
                WS[x][y] = letters[(random.randint(0,len(letters)-1))]

    print()

    PrintMatrix(WS)




    pass

if __name__ == '__main__':
    main()
