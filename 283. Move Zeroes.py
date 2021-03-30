'''
283. Move Zeroes

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

'''

def moveZeroes(nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        idx = 0
        for i in range(len(nums)):
            if(i ==len(nums)):
                return nums
                break
            i = idx
            if(nums[i] == 0):                
                nums.append(nums[i])
                nums.pop(i)
                idx = i
            else:
                idx += 1
        return nums
                

#test case 1
nums = [0,1,0,3,12]
res = moveZeroes(nums)
print(res)
