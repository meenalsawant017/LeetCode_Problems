'''

Largest K such that both K and -K exist in array

Given an array A of N integers, returns the largest integer K > 0
such that both values K and -K exist in array A. If there is no such integer,
the function should return 0.

Example 1:
Input:[3, 2, -2, 5, -3]
Output: 3
Example 2:
Input:[1, 2, 3, -4]
Output: 0

'''

def largest_k(nums):
      s = set(nums)
      result = 0
      
      for n in nums:
            if -n in nums:
                  result = max(result, n)
      
      return result


nums =  [-1, 0, 25, 1, 5, 2, 6, -1, 5, 8, 5, -2, -10]#[1, 2, 3, -4]#[3, 2, -2, 5, -3]
res = largest_k(nums)
print(res)
