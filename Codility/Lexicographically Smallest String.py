'''
Lexicographically Smallest String


Given a string str, the task is to find the lexicographically smallest string that can be formed by removing at most one character from the given string.

Example 1:
Input: abcda
Output: abcd
Example 2:
Input: abcda
Output: abca


'''

def smallest_string(s):
      for i in range(len(s) - 1):
            if s[i] > s[i + 1]:
                  print('break condition', s[i], 'next', s[i+1])
                  break
      return s[:i] + s[i + 1:]

s = 'abcda'
res = smallest_string(s)
print(res)
