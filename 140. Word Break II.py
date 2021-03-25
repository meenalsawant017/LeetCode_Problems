import collections
def wordBreak(s, wordDict):
        N = len(s) # calculate the length of the string
        
        # Initialize a dpTable, dpDict, create a set of wordDict for dater lookup
        dpTable = [True] + [False]*N
        print('dpTable', dpTable)
        dpDict = collections.defaultdict(list)
        dpDict[0] = [""]
        wordDict = set(wordDict)
        print('wordDict', wordDict)

        # implement Word Break I logic to see if the word break is possible at all
        for i in range(1, N+1):
            for loc in range(i):
                if not dpTable[loc]: continue
                word = s[loc:i]
                if word in wordDict:
                    dpTable[i] = True
                    
        if not dpTable[-1]: return []
        
        # implement the logic for Word Break II. Here we use a defaultdict to store the broken words.
        for i in range(1, N+1):
            #print('printing outer loop', i)  
            for loc in range(i):
                print('printing outer loop', i,'printing inner loop',loc)  
                if not dpDict[loc]:
                      print('Checking--> word is not present in wordDict',dpDict[i])
                      #print('Outer loop',i, 'Inner loop',loc)
                      print('')
                      continue # if this is False, then it means that the word until this index
                                             #is not present in the wordDict.
                
                word = s[loc:i]
                #print('s[loc:i]', word)
                if word in wordDict:
                    print('Word found in worddict')
                    print('dp[loc]',dpDict[loc],'dp[i]', dpDict[i])
                    dpDict[i].extend(curr + " " + word if curr else word for curr in dpDict[loc])
                    # create a sentence.
                    print('dp[loc]',dpDict[loc],'dp[i]', dpDict[i])

        return dpDict[N] # return all possible sentences.



s = "catsanddog"
wordDict = ["cat","cats","and","sand","dog"]
res = wordBreak(s, wordDict)
print(res)
