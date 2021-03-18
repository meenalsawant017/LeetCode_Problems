'''
1328. Break a Palindrome

Example 1:

Input: palindrome = "abccba"
Output: "aaccba"
Explanation: There are many ways to make "abccba" not a palindrome, such as "zbccba", "aaccba", and "abacba".
Of all the ways, "aaccba" is the lexicographically smallest.

'''

import math

def break_palindrom(s):
      for i in range(math.floor(len(s)//2)):
            if(s[i] != 'a'):
                  return s[:i] + 'a' + s[i+1:]
      if(len(s) == 1):
            return ""
      else:
            return s[:-1] + 'b'

#str1 = "abccba" 
#str1 = "a"
str1 = 'aa'
r1 =break_palindrom(str1)
print(r1)
      
