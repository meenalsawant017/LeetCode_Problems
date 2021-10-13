'''
Longest Substring Without Two Contiguous Occurrences of Letter

Given a string str containing only a and b, find the longest substring of str
such that str does not contain more than two contiguous occurrences of a and b.

Example 1:
Input: aabbaaaaabb
Output: aabbaa
Example 2:
Input: aabbaabbaabbaaa
Output: aabbaabbaabbaa

'''
def longestValidString(s):
      i = 0
      j = 1
      count = 1
      start = i
      end = j
      max_len = 0
      substr = ''

      while i <= j and j < len(s):
            if s[j-1] == s[j]:
                  count += 1
            else:
                  count = 1
                  
            if count <= 2:
                  
                  if max_len < len(s[i:j+1]):
                        substr = s[i:j+1]
                        max_len = len(s[i:j+1])
            else:
                  i = j-1
                  j = j-1
                  count = 1
            j += 1
             
                  
      return substr
      
            
s = 'aabbaaaaabb' # aabbaa
s = 'aabbaabbaabbaa' # aabbaabbaabbaa
s = 'aabbababbaabaababbababaababbabababababaaababababbabaaabbbaabbabbababababaabba'
s = 'aabbaaaaaaaccddeeff' # aaccddeeff
res = longestValidString(s)          
print(res)
