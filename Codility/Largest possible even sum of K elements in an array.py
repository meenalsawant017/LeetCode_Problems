'''
'''
We are given a list of positive integers and we have to
find the maximum even sum for K elements from the list. If we can’t find one, we return -1.

'''
def largest_sum(arr, K):
    print('Given Arr', arr)  
    N = len(arr)
    # If count of elements
    # is less than K
    if (K > N):
        return -1
 
    # Stores maximum
    # even subsequence sum
    maxSum = 0
 
    # Stores Even numbers
    Even = []
 
    # Stores Odd numbers
    Odd = []
 
    # Traverse the array
    for i in range(N):
 
        # If current element
        # is an odd number
        if (arr[i] % 2 == 1):
 
            # Insert odd number
            Odd.append(arr[i])
            #print('ODD', Odd)
 
        else:
 
            # Insert even numbers
            Even.append(arr[i])
            #print('EVEN', Even)
 
    # Sort Odd[] array
    Odd.sort(reverse=False)
 
    # Sort Even[] array
    Even.sort(reverse=False)

    print('Sorted Odd', Odd)
    print('Sorted Even', Even)
    
    # Stores current index
    # Of Even[] array
    i = len(Even) - 1
 
    # Stores current index
    # Of Odd[] array
    j = len(Odd) - 1
 
    while (K > 0):
 
        # If K is odd
        if (K % 2 == 1):
            print('k is odd')  
 
            # If count of elements
            # in Even[] >= 1
            if (i >= 0):

                print('i:', i)
                # Update maxSum
                maxSum += Even[i]
                
                # Update i
                i -= 1
 
            # If count of elements
            # in Even[] array is 0.
            else:
                return -1
 
            # Update K
            K -= 1
            print('maxSum:', maxSum, "i", i, 'K:', K)
 
        # If count of elements
        # in Even[] and odd[] >= 2
        elif (i >= 1 and j >= 1):
            if (Even[i] + Even[i - 1] <=
                    Odd[j] + Odd[j - 1]):
 
                # Update maxSum
                maxSum += Odd[j] + Odd[j - 1]
 
                # Update j.
                j -= 2
 
            else:
 
                # Update maxSum
                maxSum += Even[i] + Even[i - 1]
 
                # Update i
                i -= 2
 
            # Update K
            K -= 2
 
        # If count of elements
        # in Even[] array >= 2.
        elif (i >= 1):
 
            # Update maxSum
            maxSum += Even[i] + Even[i - 1]
 
            # Update i.
            i -= 2
 
            # Update K.
            K -= 2
 
        # If count of elements
        # in Odd[] array >= 2
        elif (j >= 1):
 
            # Update maxSum
            maxSum += Odd[j] + Odd[j - 1]
 
            # Update i.
            j -= 2
 
            # Update K.
            K -= 2
 
    return maxSum
 
      
#test case 1
arr = [4,9,8,2,6] # 18 
k = 3
print(largest_sum(arr,k))

#test case 2
arr = [5,6,3,4,2]
k = 5
print(largest_sum(arr,k)) #20

#test case 2
arr = [10000]
k = 2
print(largest_sum(arr,k)) #-1

#test case 2
arr = [2,3,3,5,5]
k = 3
print(largest_sum(arr,k)) # 12 

arr=[4, 2, 6, 7, 8]
k = 3
print(largest_sum(arr,k)) #18

arr= [5, 5, 1, 1, 3]
k = 3
print(largest_sum(arr,k)) #-1

