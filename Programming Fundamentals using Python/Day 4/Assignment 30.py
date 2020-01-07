'''
Given a string containing uppercase characters (A-Z), compress the string using Run Length encoding. Repetition of character has to be replaced by storing the length of that run.

Write a python function which performs the run length encoding for a given String and returns the run length encoded String.

Provide different String values and test your program.

Sample Input	Expected Output
AAAABBBBCCCCCCCC	4A4B8C
AABCCA	2A1B2C1A
'''

#PF-Assgn-30
def encode(message):
    count = 0
    chatacter = ''
    previous_char = message[0]
    result = ''
    length = len(message) 
    i = 0
    while (i != length ):
        chatacter = message[i]
        
        if previous_char == chatacter :
            count = count + 1
        else :
            result = result + str(count) + previous_char
            count = 1
        previous_char = chatacter
        i = i + 1
    return result + str(count) + str(previous_char)
encoded_message=encode("ABBBBCCCCCCCCAB")
print(encoded_message)
