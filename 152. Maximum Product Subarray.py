'''
152. Maximum Product Subarray


Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

'''

def maxProduct(nums):
        local_max = local_min = global_max = nums[0]
                        
        for n in nums[1:]:
            temp = local_max
            local_max = max(n, n*local_max , n*local_min)
            local_min = min(n, n*local_min, n*temp)
            global_max = max(global_max , local_max)
        return global_max

nums = [2,3,-2,4]
res = maxProduct(nums)
print(res)
