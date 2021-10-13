def minDeletions(s):
        d= {}
        max_sum = 0
        unique = set()
        count = 0

        for i in s:
            if i not in d:
                  d[i] = 0
            d[i] += 1
        #print(d)

        for k,v in d.items():
            
            while v in unique:
                v -= 1
                count += 1
            if v > 0:
                unique.add(v)
    
        return count
            
      
s = 'aaabbbcc' # 2
s = 'aab' # 0
s = 'ceabaacb' #2
print(minDeletions(s))
