'''
Given a list of strings string_list and a list of words words, determine whether each word in words
can be formed as a concatenation of consecutive strings in string_list starting with index 0.
ex. word = "oneTwoThree", string_list = ["one", "Three", "Two"] is false because the words aren't consecutive in string_list
ex. word = "one", string_list = ["one", "Three", "Two"] is True because the concatenation stops at the first index in string_list
ex. word = "one", string_list = ["One", "one", "Two"] is False because the concatenation doesn't start at 0.
'''
def is_consecutive(word, string_list):
    res = ''
    for w in string_list:
        res += w
        if res == word:
            return True
    return False


#word = "oneTwoThree"
#string_list = ["one", "Three", "Two"]
#word = "one"
#string_list = ["one", "Three", "Two"] 
word = "one"
string_list = ["One", "one", "Two"] 
print(is_consecutive(word, string_list))
