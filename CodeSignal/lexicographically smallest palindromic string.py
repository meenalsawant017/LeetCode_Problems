"""
Given a string s, return the longest and lexicographically smallest palindromic string
that can be formed from the characters.

ex. "abbaa" -> "abba"
ex. "adeadeadevue" -> "adeeaeeda"
"""
def smallestPalindrome(s):
      for i in range(len(s) - 1):
            if s[i] > s[i + 1]:
                  break
      return s[:i] + s[i + 1:]
      


#A = "abbaa"
A = 'adeadeadevue'
print(smallestPalindrome(A)) # abba
import collections
def smallestPalindrome(str):
    store = collections.Counter(str)
    lexic_store = [[key,val] for key,val in sorted(store.items(), key=lambda x:x[0]) if val > 1]
    lexic_store_single = [[key,val] for key,val in sorted(store.items(), key=lambda x:x[0]) if val % 2 == 1][0][0]

    res = ''
    for key,val in lexic_store:
        res += (key * int(val/2))
    return res + lexic_store_single + res[::-1]

str = "abbaa"
print(smallestPalindrome(str))
str = "adeadeadevue"
print(smallestPalindrome(str))
