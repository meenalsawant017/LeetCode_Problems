#https://leetcode.com/problems/partition-to-k-equal-sum-subsets/
def canPartitionKSubsets(nums, k):
        nums = [4,3,2,3,5,2,1]
        k = 4

        total = sum(nums)
        output = []    
        row = (len(nums))
        col = k
        
        dp = [[False for x in range(col+1)] for i in range(row+1)]
        
        
        for i in range(1, row):
            dp[i][0] = True
            for j in range(1, col):
                if j-nums[i-1] >= 0:
                    dp[i][j] = ((dp[i-1][j-nums[i-1]]) or (dp[i-1][j]))
                    
                else:
                    dp[i][j] = dp[i-1][j]
                    
        print(output)
        return dp[-1][-1]

nums = [4,3,2,3,5,2,1]
k = 4
print(canPartitionKSubsets(nums, k))
