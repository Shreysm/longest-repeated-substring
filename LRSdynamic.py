#Author: Shreyas Mohan

import sys


#LRS method returns a matrix containing the length of all possible subsequences
def LRS(inputString):
    #L is a two dimension array containing the lengths of subsequences
    L = []
    #L is initially defined as 0 for all positions
    L = [[0 for i in range(length + 1)] for j in range(length + 1)]
    #First row and First column in the array will contain value as 0
    for i in range(1, length + 1):
        flag = 0
        for j in range(1, length + 1):
            #When the last characters match,the diagonal cell value is incremented by 1
            if (inputString[i - 1] == inputString[j - 1] and i != j and flag == 0):
                L[i][j] = L[i - 1][j - 1] + 1
                flag=1
            #When the last characters does not match,maximum value among the top and left cell is taken 
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])
    return L

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


L = LRS(inputString)

i = length
j = length
final = ''
count=0
#To extract the longest repeated subsequence using bottom up approach
while (i > 0 and j > 0):
    #Checking if the value obtained is equal to 1 increment of the diagonal cell
    if (L[i][j] == L[i - 1][j - 1] + 1):
        final += inputString[i - 1]
        i -= 1
        j -= 1
        count=1
    #Comparing the cell value to its top cell
    elif (L[i][j] == L[i - 1][j]):
        i -= 1
    #Comparing the cell value to its left cell
    else:
        j -= 1
#Reverse the string obtained
final = ''.join(reversed(final))
    
if (count==0):
    print("Input String has no repeated characters")
    sys.exit()   
        
    


print "Longest Repeated Subsequence: ",final


