#https://leetcode.com/discuss/interview-question/891655/postmates-oa-rectangle-boxes
def Rectangle_Boxes(operations):
      n = len(operations)
      dp = [False] * (n+1)
      dp[0] =  True
      dp[1] =  True
      print(dp)

      for i in range(1, n):
            h_curr = operations[i][2]
            w_curr = operations[i][1]
            for j in range(i):
                  h_rev = operations[j][2]
                  w_rev = operations[j][1]
                  #print('height:',height,'width:',width)
                  if h_curr >= h_rev and w_curr >= w_rev:
                        dp[j] = dp[i] and True
      print(dp)
            

      


operations =  [[0, 1, 3], [0, 4, 2], [1, 3, 4], [1, 3, 2]]
print(Rectangle_Boxes(operations))
