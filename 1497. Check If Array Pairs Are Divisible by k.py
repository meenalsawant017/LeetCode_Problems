'''
1497. Check If Array Pairs Are Divisible by k

Example 1:

Input: arr = [1,2,3,4,5,10,6,7,8,9], k = 5
Output: true
Explanation: Pairs are (1,9),(2,8),(3,7),(4,6) and (5,10).

'''
import collections
from collections import Counter

def canArrange(arr,k):
      d = {}
      for i in arr:
            t = i % k
            if t not in d:
                d[t] = 1 
            else:
                d[t] += 1 
      print(d)
      for key,v in d.items():
            #print('key,val', key,v)
            if key == 0:
                print('key == 0')
                if v % 2 == 0:
                    continue 
                else:
                    return False
            if k-key not in d:
                print('k-key')
                return False 
            if d[k-key] != v:
                print(key)
                print('d[k-key]')
                return False 
      return True



arr = [1,2,3,4,5,10,6,7,8,9]
k = 5

#test case 2
#arr = [92, 75, 65, 48, 45, 35]#[1,2,3,4,5,6]
#k = 10

#test case 3
#arr = [1,2,3,4,5,6]
#k = 7

res = canArrange(arr, k)
print(res)
