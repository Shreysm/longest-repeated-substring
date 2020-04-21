#Author: Shreyas Mohan

import sys

#counting the times that letter present in input
def characterCount(characterList, key):
    count = 0
    for character in characterList:
        if (character == key):
            count = count + 1
    return count


#Checking if the input string is provided in the command line arguments    
if(len(sys.argv)<2):
    print("No input string given!Try again!")
    sys.exit()
#Store the input string
inputString = str(sys.argv[1])

length = len(inputString)
#Minimum length of input string must be two
if (length <2):
    print("Input should contain 2 or more characters")
    sys.exit()

#characterList is the list of characters in the input string    
characterList = []
characterList = inputString

#repeatedCharcters will contain the list of unique characters repeated in the input string
repeatedCharacters = []

#Finding the repeated characters in the sequence through iteration
for i in range(length):
    characterFrequency = characterCount(inputString,inputString[i])
    if(characterFrequency > 1):
        if inputString[i] not in repeatedCharacters:
            repeatedCharacters.append(inputString[i])
    

final=''
#Convert the list into a string
for i in range(len(repeatedCharacters)):
    final = final+repeatedCharacters[i]
if final=='':
    print "Input String has no repeated characters"
else:
    print "Longest Repeated Sequence: ",final

