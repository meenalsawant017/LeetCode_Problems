def max_sum(arr):

      d = {}
      max_sum = 0

      for i in arr:
            tmp = 0
            ch = str(i)
            for j in ch:
                  tmp += int(j)
            if tmp not in d:
                  d[tmp] = []
            d[tmp].append(i)
      print(d)

      for k,v in d.items():
            val = sorted(v, reverse = True)
            max_sum = max(max_sum, sum(val[:2]))
            
      print(max_sum)

      if len(arr) == len(d):
            return -1

arr = [51, 32, 43] #-1
#arr = [42, 33, 60] # 102
#arr = [51, 71, 17, 42] #93
print(max_sum(arr))
