'''
1051. Height Checker

Example 1:

Input: heights = [1,1,4,2,1,3]
Output: 3
Explanation: 
Current array : [1,1,4,2,1,3]
Target array  : [1,1,1,2,3,4]
On index 2 (0-based) we have 4 vs 1 so we have to move this student.
On index 4 (0-based) we have 1 vs 3 so we have to move this student.
On index 5 (0-based) we have 3 vs 4 so we have to move this student.

'''
def heightChecker(heights):
        #heights = [5,1,2,3,4]
        sort_height = sorted(heights)
        counter = 0
        for i , j in zip(heights, sort_height):
            if(i != j):
                counter += 1
        return counter

heights = [1,1,4,2,1,3]
res = heightChecker(heights)
print(res)
