def wordBreak(s, wordDict):
	
        # regular dp initalization
        n = len(s)
        dp = [False for _ in range(n+1)]
        
        # base case(can decompose empty string)
        dp[0] = True
        
        # two pointers dp tech
		# outer loop = upper substring
		# inner loop = inner substring
		
        for i in range(1,n+1):
            for j in range(0,i):
                
                # if lower-substring can be decomposed
                # and upper substring is in dictonary 
                if dp[j] and s[j:i] in wordDict:
                    output.append(s[j:i])
                    dp[i] = True
                    break
        return dp[-1]
'''s = 'code'
wordDict ={'c','od','d','e'}'''

#test case 2
s = 'leetcode'
wordDict = ["leet","code"]


res = wordBreak(s, wordDict)
print(res)
