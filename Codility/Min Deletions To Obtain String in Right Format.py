'''

Min Deletions To Obtain String in Right Format

    ij
YXXXYXY

'''

def minStep(s):
      charX = 'X'
      numY = 0
      minDel = 0
 
      for i in range(len(s)):
            if charX == s[i]:
                  minDel = min(numY, minDel + 1)
            else:
                  numY += 1
      return minDel

s = 'YXXXYXY' #2
s = 'XXYYYY' #0
res = minStep(s)
print(res)
