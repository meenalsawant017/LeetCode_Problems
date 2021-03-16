'''
516. Longest Palindromic Subsequence

Example 1:

Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".

'''

def longestPalindromeSubseq(s):
        rev = s[::-1]
        m = len(s)
        n = len(rev)
        table = [[None] * (n+1) for i in range(m+1)]
        
        for i in range(m+1):
            for j in range(n+1):
                if(i == 0 or j == 0):
                    table[i][j] = 0
                elif(s[i-1] == rev[j-1]):
                    table[i][j] = 1 + table[i-1][j-1]
                else:
                    table[i][j] =max(table[i-1][j], table[i][j-1])
        return table[i][j]

s = "bbbab"
res = longestPalindromeSubseq(s)
print(res)
