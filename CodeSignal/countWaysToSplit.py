def countWaysToSplit(s):
   lenS = len(s)
   count = 0

   for i in range(1,lenS-1):
      for j in range(i+1, lenS):
            ab = s[0:i]
            bc = s[i:j]
            ca = s[j:]
            if ab != bc and bc != ca  and ca != ab :
                count += 1 
   return count

s = 'xzxzx'
res = countWaysToSplit(s)
print(res)
 
s = 'xzxzxzxzxz' #30
print("")
print('string: ', s)
print(countWaysToSplit(s))

s = 'xxxxxxxxxx' #24
print("")
print('string: ', s)
print(countWaysToSplit(s))

s = 'gggggggggggggggggggggggggggggg' # 366
print("")
print('string: ', s)
print(countWaysToSplit(s))

s = 'gfgfgfgfgfgfgfgfgfgfgfgfgfgfgf' #387
print("")
print('string: ', s)
print(countWaysToSplit(s))
