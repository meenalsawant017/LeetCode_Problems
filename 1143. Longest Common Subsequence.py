'''
1143. Longest Common Subsequence

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.

'''

def longestCommonSubsequence(text1, text2):
        m = len(text1)
        n = len(text2)
        
        table = [[None] * (n+1) for i in range(m+1)]
        
        for row in range(m+1):
            for col in range(n+1):
                if(row== 0 or col == 0):
                    table[row][col] = 0
                elif(text1[row - 1] ==  text2[col - 1]):
                    table[row][col] = table[row - 1][col - 1] + 1
                else:
                    table[row][col] = max(table[row -1][col], table[row][col - 1])
        return table[row][col]
      
text1 = "abcde"
text2 = "ace" 

res = longestCommonSubsequence(text1, text2)
print(res)
