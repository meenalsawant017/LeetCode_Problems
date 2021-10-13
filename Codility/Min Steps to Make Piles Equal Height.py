'''
Min Steps to Make Piles Equal Height

Given N piles of equal or unequal heights.
In one step, You can remove any number of boxes from the pile
which has the maximum height and try to make it equal to the
one which is just lower than the maximum height of the stack.
Determine the minimum number of steps required to make all
of the piles equal in height.

Example 1:
Input: [5, 2, 1]
Output: 3
Explanation:
Step 1: reducing 5 -> 2 = [2, 2, 1]
Step 2: reducing 2 -> 1 = [2, 1, 1]
Step 3: reducing 2 -> 1 = [1, 1, 1]

'''
def min_steps(nums):
      counter = 0

      for i in range(1, len(nums)):
            j = i - 1

            while j >= 0 and nums[i] < nums[j]:
                  nums[j] = nums[i]
                  j -= 1
                  counter += 1
      return counter
      

nums = [5, 2, 1] #3
#nums = [5, 5, 1] #2
#nums = [5, 5, 5, 5, 1] # 4
#nums = [3, 2, 2] #1
#nums = [5, 5, 2, 2, 1, 1] #6
res = min_steps(nums)
print(res)
