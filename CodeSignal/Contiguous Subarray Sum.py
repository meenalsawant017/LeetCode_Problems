#https://algodaily.com/challenge_slides/contiguous-subarray-sum/tests
def subarray_sum(nums, n):
    
    def dfs(idx, subarray):
      i = idx+1
      while i < len(subarray):
        total = subarray[idx] + subarray[i]
        if total == n:
          return True
        elif total > n:
          return
        i += 1
          
    
    for i in range(len(nums)):
      res = dfs(i, nums[i:])
      if res == True:
        return True
    return False

nums = [3, 6, 12, 35]
n = 47
print(subarray_sum(nums, n))
