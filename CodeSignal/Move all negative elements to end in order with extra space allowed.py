def move_negNumbers(nums):
      end = len(nums)-1

      for i in range(len(nums)-1, -1, -1):
            if nums[i] < 0:
                  temp = nums[end]
                  nums[end] = nums[i]
                  nums[i] = temp
                  end -= 1
      return nums
            

nums = [1,2,-3,-5,2,7,-9,-11]
                    
print(move_negNumbers(nums))
