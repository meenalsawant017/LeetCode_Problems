"""/*************************************************************************
 *
 *  Algorithms and Computing Theory
 *
 *  Problem: Longest Substring Without Repeating Characters
 *  Description: Given a string , find the length of the longest substring without repeating characters.
 *
 *  Input: s = "abcabcbb"
 *  Output: 3
 *  Explanation: The answer is "abc", with the length of 3.
 
 *************************************************************************/"""

import collections 

def lengthOfLongestSubstring(s):
        longest_string = collections.deque()
        res = 0
        l,r = 0,0
        
        while l < len(s):
            if s[l] not in longest_string:
                longest_string.append(s[l])
                l+=1                
            else:                
                longest_string.popleft()                
                r += 1

            res = max(res, l - r)
        return res

string = 'abcabcbb'
result = lengthOfLongestSubstring(string)
print(result)
