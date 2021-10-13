def fairIndexes(A,B):
    
    for i in range(1, len(A)):
        A[i] += A[i - 1]
        B[i] += B[i - 1]
    print('Sorted--->', 'A:',A,'B:',B)

    fair = 0
    for k in range(1, len(A)):
        left_A, right_A = A[k - 1], A[-1] - A[k - 1]
        #print('left_A:',left_A,'right_A:', right_A)
        #print(' A[-1] ',  A[-1] ,'A[k - 1]', A[k - 1])
        left_B, right_B = B[k - 1], B[-1] - B[k - 1]
        #print('left_B:',left_B,'right_B:', right_B)
        if(left_A == right_A == left_B == right_B):
            fair += 1
            
        print('fair:',fair)
    return fair

#A = [4, -1, 0, 3]
#B = [-2, 5, 0, 3]
A = [2, -2, -3, 3]
B = [0, 0, 4, -4]

res = fairIndexes(A,B)
print(res)
