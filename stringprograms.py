def reverseString(st):
    st1 = trimString(st)
    return st1[::-1]

def trimString(st):
    return st.strip()

def lengthOfString(st):
    return len(st)

def countNumeric(st):
    st1 = trimString(st)
    count = 0
    for ch in st1:
        if(ch.isdigit()):
            count+=1
    return count

def countAlphabets(st):
    st1 = trimString(st)
    count = 0
    for ch in st1:
        if(ch.isalpha()):
            count+=1
    return count

def countAlphaNumeric(st):
    st1 = trimString(st)
    count_of_digit = countNumeric(st1)
    count_of_alphabets = countAlphabets(st1)
    return count_of_digit+count_of_alphabets

def countSpecialCharacters(st):
    st1 = trimString(st)
    count_of_digit = countNumeric(st1)
    count_of_alphabets = countAlphabets(st1)
    return (lengthOfString(str) - (count_of_digit+count_of_alphabets))

str = "Hello! How are you doing today? I'm learning Python 101, it's fun! :) #Python# 1234 @ #@  version 1.2345   "

print('Total Length of String : ',lengthOfString(str))
print('Total Length of Alphabets in the string : ',countAlphabets(str))
print('Total Length of Digit in the string : ',countNumeric(str))
print('Total Length of AlphaNumeric in the string : ',countAlphaNumeric(str))
print('Total Length of SpecialCharacters in the string : ',countSpecialCharacters(str))
print('Total Length of SpecialCharacters in the string : ',str.count('python'))