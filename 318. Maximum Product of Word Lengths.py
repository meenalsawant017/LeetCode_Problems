'''
318. Maximum Product of Word Lengths

Example 1:

Input: words = ["abcw","baz","foo","bar","xtfn","abcdef"]
Output: 16
Explanation: The two words can be "abcw", "xtfn".
'''

def maxProduct(words):
      notcommon =0
      n = len(words)
      for i in range(n-1):
            for j in range(i+1,n):
                  if(set(words[i]).isdisjoint(set(words[j]))):
                        if(len(words[i])*len(words[j])>notcommon):
                              notcommon = len(words[i])*len(words[j])
            
      return notcommon

words = ["abcw","baz","foo","bar","xtfn","abcdef"]

res = maxProduct(words)
print(res)
