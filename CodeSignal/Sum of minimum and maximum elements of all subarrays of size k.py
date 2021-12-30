def minMaxSubArray(nums, k):
        curr_total = 0
        globalMax = 0
        output = []
        
        for i in range(len(nums)):
            temp = nums[i : i+k]
            min_ = min(temp)
            max_ = max(temp)
            curr_total = min_ + max_
            if len(nums[i : i+k]) == k:
                  globalMax += curr_total
        return globalMax
      
nums = [5, 9, 8, 3, -4, 2, 1, -5]
k = 4
print(minMaxSubArray(nums, k))

nums = [1, -1, 2, -2, 3, -3]
k = 2
print(minMaxSubArray(nums, k))


