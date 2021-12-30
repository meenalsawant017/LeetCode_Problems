def threeWayPartition(arr, n, lowVal, highVal):
 
    # Initialize ext available positions for
    # smaller (than range) and greater elements
    start = 0
    end = n - 1
    i = 0
 
    # Traverse elements from left
    while i <= end:
 
        # If current element is smaller than
        # range, put it on next available smaller
        # position.
        if arr[i] < lowVal:
            temp = arr[i]
            arr[i] = arr[start]
            arr[start] = temp
            i += 1
            start += 1
 
        # If current element is greater than
        # range, put it on next available greater
        # position.
        elif arr[i] > highVal:
            temp = arr[i]
            arr[i] = arr[end]
            arr[end] = temp
            end -= 1
 
        else:
            i += 1
 
# Driver code
if __name__ == "__main__":
    '''arr = [1, 14, 5, 20, 4, 2, 54,
           20, 87, 98, 3, 1, 32]
       lowValue = 10
       highValue = 20
    '''

    arr = [2,5,87,56,12,4,9,23,76,1,45] 
    lowValue = 15
    highValue = 30

    n = len(arr)
 
    threeWayPartition(arr, n, lowValue, highValue)
 
    print("Modified array")
    for i in range(n):
        print(arr[i], end = " ")
