def longestConsecutive(nums):
        #create set
        numset = set(nums)
        
        #Date variable
        global_max = 0
        current_max = 0
        
        for n in nums:
            if n-1 not in numset:
                #print('not in set', n-1)
                current_max = 0
                while n + current_max in numset:
                    #print('n+current_max', n+ current_max)
                    #print(numset, current_max,n + current_max)
                    current_max += 1
                    global_max = max(global_max, current_max)
                    
        return global_max

print(longestConsecutive([100,4,200,1,3,2]))
