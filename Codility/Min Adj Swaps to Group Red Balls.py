'''

Min Adj Swaps to Group Red Balls
Given string S of length N built from characters "R" and "W", representing red and white balls respectively, returns the minimum number of swaps needed to arrange all the red balls into a consistent segment. If the result exceeds 10^9, return -1.

Example 1:
Input:WRRWWR
Output: 2
Explanation:
We can move the last ball two positions to the left:

swap R and W -> WRRWRW
swap R and W -> WRRRWW
Example 2:
Input:WWRWWWRWR
Output: 4
Explanation:
We can move the last ball two positions to the left:

swap R and W -> WWRWWWRRW
swap R and W -> WWWRWWRRW
swap R and W -> WWWWRWRRW
swap R and W -> WWWWWRRRW
Example 3:
Input:WR
Output: -1
Explanation:
The minimum needed number of swaps is greater than 10^9. So return -1.

Example 4:
Input:WWW
Output: 0

'''

def min_swaps(s):

      if 'R' not in s:
            return 0
      first = s.index('R')
      last = 0
      swaps = 0

      for i in range(len(s)):
            if s[i] == 'R':
                  swaps += 1
                  last = i
                  
      if last == first:
            return -1
      else:
            return last - first - swaps + 1
            

#s = 'WWRWWWRWR'
s = 'WRRWWR'
#s ='WWRWWWRRW'
res = min_swaps(s)
print(res)
