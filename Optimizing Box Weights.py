'''
Optimizing Box Weights

Example 1:
Input:
nums = [4, 5, 2, 3, 1, 2]

Output:
[4, 5]


'''


def minimalHeaviestSetA(arr):
    subsetA = []
    total_sum = sum(arr)
    arr.sort(reverse=True)
    maxsum = 0
    while True:
        if maxsum > total_sum:
            break
        else:
            ele_pop = arr.pop(0)
            subsetA.insert(0, ele_pop)
            total_sum -= ele_pop
            maxsum += ele_pop
    return subsetA;

#nums = [4, 5, 2, 3, 1, 2]
nums = [3, 7, 5, 6, 2]
res1 =optimizing_boxes(nums)
res = minimalHeaviestSetA(nums)
print(res1)
print(res)
