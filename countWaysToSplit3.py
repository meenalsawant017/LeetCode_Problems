def countWaysToSplit3(s):
   listS= list(s)
   # print (listS)
   lenS = len(listS)
   count = 0

   for i in range(1,lenS):
      for j in range(i+1, lenS):
            ab = s[0:j]
            bc = s[i:lenS]
            ca = s[j:lenS]
            print("AB is :",ab,"BC is:",bc,"CA is:",ca)
            if ab != bc and bc != ca  and ca != ab :
                count += 1 
                print(count)  
   return count

s = 'xzxzx'
res = countWaysToSplit3(s)
print(res)
