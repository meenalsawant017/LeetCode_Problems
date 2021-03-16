def sortedSquares(nums):
        square = []
        for i in range(len(nums)):
            j = nums[i] * nums[i]
            square.append(j)
            #print(j)
        return sorted(square)

nums = [-4,-1,0,3,10]
res = sortedSquares(nums)
print(res)
