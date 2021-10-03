'''
https://leetcode.com/discuss/interview-question/1381710/Uber-or-OA-or-2021-or-Code-Signal
'''
def duplicatePairs(nums, k):         # sliding window O(N)
    seen, res = set(), 0
    i = j = len(nums) - 1
    while i >= 0:                    # prepare to expand the window till containing k duplicate pairs
        if nums[i] in seen: 
            k -= 1
            seen.remove(nums[i])
            print('seen', seen, i) 
        else:
            seen.add(nums[i])
            print('add', seen,i)
            print('k:', k)
        while not k:                 # prepare to shrink the window when containing k duplicate pairs
            print('k is zero')
            res += i + 1
            if nums[j] in seen:
                seen.remove(nums[j])
            else:
                k += 1
                seen.add(nums[j])
            j -= 1                   # ready to shrink
        i -= 1                       # ready to expand
    return res

nums = [2,2,2,2,2,2]
k = 3
print(duplicatePairs(nums, k))
