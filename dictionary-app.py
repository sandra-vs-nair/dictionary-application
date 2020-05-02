# -----------------------------------------------------------
# A simple dictionary application using python.
#
# (C) 2020 Sandra VS Nair, Trivandrum
# email sandravsnair@gmail.com
# -----------------------------------------------------------

import json
import sys
import difflib

# @desc Returns the meaning of a word if found. Else, queries the user with similar words.
# If no similar words are found, displays a suitable message and exit the program.
# @param string $word - the word to which meaning is sought.
# @return void.


def definition(word):
    word=word.strip()      #Remove leading and trailing spaces.
    if word.lower() in data or word.title() in data or word.upper() in data:  
        num,meanings= len(data[word]),data[word]
        i=1
        for meaning in meanings:
            print(i, meaning)
            i=i+1
    else:
        print("The word does not exist")
        similar_word=difflib.get_close_matches(word,data.keys(),1,0.7)  #Checking for similar words.
        if not similar_word:                                            #No similar words found.
            print("No similar words found. Please check and try again")
            sys.exit()
        response=input("Do you mean "+similar_word[0]+" ? Y or N ?")
        if response == 'Y' or response =='y':
            definition(similar_word[0])
        elif response == 'N' or response =='n':
            print("Please make sure of the spelling and type again")
            sys.exit()
        else:
            print("Please type Y or N")
data = json.load(open("data/dictionary.json"))    #Loading the dictionary file.
word=input("Enter a word :")
definition(word)
