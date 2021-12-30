def maxSubArray(nums, k):
        curr_total = 0
        minSum = 999999
        output = []
        
        for i in range(len(nums)):
            curr_total = sum(nums[i : i+k])
            
            if len(nums[i : i+k]) == k and (curr_total <  minSum):
                minSum = curr_total
                output = nums[i : i+k]                  
        return output
      
nums= [42, 20, 15, 26, 10, 33]
k = 3
print(maxSubArray(nums, k))

