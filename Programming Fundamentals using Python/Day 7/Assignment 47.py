'''
Write a python function, encrypt_sentence() which accepts a message and encrypts it based on rules given below and returns the encrypted message.

Words at odd position -> Reverse It
Words at even position -> Rearrange the characters so that all consonants appear before the vowels and their order should not change

Note: 
1.	Assume that the sentence would begin with a word and there will be only a single space between the words.
2.	Perform case sensitive string operations wherever necessary.
Also write the pytest test cases to test the program.


Sample Input	Expected Output
the sun rises in the east	eht snu sesir ni eht stea
'''
#PF-Assgn-47
def encrypt_sentence(sentence):
    sentence=sentence.split()
    res=""
    for i in range(len(sentence)):
        if i%2==0:
            word=sentence[i]
            reverse=word[::-1]
            res+=reverse+" "
        else:
            vowels="aeiouAEIOU"
            word=sentence[i]
            vowel=""
            non_vowel=""
            for w in word:
                if w in vowels:
                    vowel+=w
                else:
                    non_vowel+=w
            res+=non_vowel+vowel+" "   
    return res
            
    
sentence="The sun rises in the east"
encrypted_sentence=encrypt_sentence(sentence)
print(encrypted_sentence)
