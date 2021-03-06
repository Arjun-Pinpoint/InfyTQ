'''
Write python function, sms_encoding() which accepts a sentence and converts it into an abbreviated sentence to be sent as SMS and returns the abbreviated sentence.

Rules are as follows:
a. Spaces are to be retained as is
b. Each word should be encoded separately
•	If a word has only vowels then retain the word as is
•	If a word has a consonant (at least 1) then retain only those consonants

Note: Assume that the sentence would begin with a word and there will be only a single space between the words.

Sample Input	Expected Output
I love Python	I lv Pythn
MSD says I love cricket and tennis too	MSD sys I lv crckt nd tnns t
I will not repeat mistakes	I wll nt rpt mstks
'''
#PF-Assgn-50

def sms_encoding(data):
    data=data.split()
    res=""
    for i in data:
        if len(i)!=1:
            for j in i:
                if j not in "aeiouAEIOU":
                    res+=j
        res+=" "
    return res

data="I love Python"
print(sms_encoding(data))
