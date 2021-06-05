"""
You are given an array of distinct integers arr and an array of integer arrays pieces, where the integers in pieces are distinct. Your goal is to form arr by concatenating the arrays in pieces in any order. However, you are not allowed to reorder the integers in each array pieces[i].

Return true if it is possible to form the array arr from pieces. Otherwise, return false.

Example 1:

Input: arr = [85], pieces = [[85]]
Output: true
"""

from collections import deque

def canFormArray(arr, pieces):
        hmap = {arr[a]:a for a in range(len(arr))}
        for i in range(len(pieces)):
            if len(pieces[i])>1:
                for k in range(len(pieces[i])-1):
                    if pieces[i][k] not in hmap or pieces[i][k+1] not in hmap:
                        return False
                    if hmap[pieces[i][k+1]]-hmap[pieces[i][k]]>1 or hmap[pieces[i][k]]>hmap[pieces[i][k+1]]:
                        return False
            else:
                if pieces[i][0] not in hmap:
                    return False
        return True

      
"""
Given a list of strings string_list and a list of words words, determine whether each word in words
can be formed as a concatenation of consecutive strings in string_list starting with index 0.
ex. word = "oneTwoThree", string_list = ["one", "Three", "Two"] is false because the words aren't consecutive in string_list
ex. word = "one", string_list = ["one", "Three", "Two"] is True because the concatenation stops at the first index in string_list
ex. word = "one", string_list = ["One", "one", "Two"] is False because the concatenation doesn't start at 0.
Just use the base idea from the LeetCode problem and then modify it for the consecutive concatenation requirement.
It's actually easier than the LeetCode problem.
"""

def isConcatenate(word, string_list):
    res = ''
    for w in string_list:
        res += w
        if res == word:
            return True
    return False

        
arr = [2,82,79,95,28]
pieces = [[2],[82],[28],[79,95]]
res = canFormArray(arr, pieces)
print(res)

word = "oneTwoThree"
string_list = ["one", "Three", "Two"] 
res = isConcatenate(word, string_list)
print(res)

