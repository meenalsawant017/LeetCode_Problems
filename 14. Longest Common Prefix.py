'''
14. Longest Common Prefix

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

'''

def longestCommonPrefix(strs):
      result = ''
        
      for i in zip(*strs):
            if((0 <= len(strs) <= 200)):# and (0 <= len(i) <= 200)):
                if min(i)== max(i):
                    result += i[0]
                else:
                    break
        
      return result

strs = ["flower","flow","flight"]
res = longestCommonPrefix(strs)
print(res)
