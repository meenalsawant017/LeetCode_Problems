'''

Unique Integers That Sum Up To 0

Given an integer n, return any array containing n unique integers
such that they add up to 0.

Example 1:
Input:5
Output: [-4,-2,0,2,4]
Example 2:
Input:3
Output: [-2, 0, 2]
Example 1:
Input:1
Output: [0]

'''
def sumZero(n):
        quotient, remainder = divmod(n, 2)
        #print('quotient:', quotient, 'remainder:', remainder)
        output = []        
        if remainder:
            output.append(0)
            #print('if output:-', output)
        
        for x in range(1, quotient + 1):
            output.extend([x, -x])
            #print('output:-', output)
        
        return output
def unique_sum(n):
      result = []

      for i in range(n):
            result.append(i * 2 - n + 1) 
      return result

n = 5
res = unique_sum(n)
print(res)
print(sumZero(n))
