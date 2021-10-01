"""
Given a string s, return the longest and lexicographically smallest palindromic string
that can be formed from the characters.

ex. "abbaa" -> "abba"
ex. "adeadeadevue" -> "adeeaeeda"
"""
import collections
def smallestPalindromeOP(s):
    if not s:
        return s
    res = []
    counts = collections.Counter(s)
    print('counts:', counts)
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    middle_letter = ""
    for letter in alphabet:
        #count = counts.get(letter, 0)
        if letter in counts:
              count = counts[letter]
        else:
              count = 0
        if count > 0:
            if count % 2 == 1 and middle_letter == "":
                middle_letter = letter
                print('mid:', middle_letter)
                res.append(letter * ((count - 1) // 2))
                print('first-->',res)
            else:
                res.append(letter * (count // 2))
                print('sec->',res)
    print(res)
    first = "".join(res)

    return first + middle_letter + first[::-1]

print(smallestPalindromeOP('adeadeadevue'))


          


