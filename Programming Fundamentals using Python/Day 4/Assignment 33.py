'''
Write a python program to display all the common characters between two strings. Return -1 if there are no matching characters.
Note: Ignore blank spaces if there are any. Perform case sensitive string comparison wherever necessary.


Sample Input	Expected output
"I like Python"
"Java is a very popular language"	lieyon
'''
#PF-Assgn-33

def find_common_characters(msg1,msg2):
    res=""
    for i in msg1:
        for j in msg2:
            if i==j:
                if i not in res:
                    res+=i
    return res
msg1="I like Python"
msg2="Java is a very popular language"
common_characters=find_common_characters(msg1,msg2)
print(common_characters)
