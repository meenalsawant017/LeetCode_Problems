"""
Given an array A return an output array B of size [A.length - 2] where B[i] = 1 if sides
A[i],A[i+1] and A[i+2] form a triangle. Otherwise, set B[i] = 0.
ex. A = [1, 2, 2, 5, 5, 4] should return B = [1,0,0,1]
"""
def validTriangle(A):
    B = []; i=0
    while i < len(A) - 2:
        a,b,c = A[i], A[i+1], A[i+2]

        if a+b>c and b+c>a and a+c>b:
            #print('appending 1 in B: a,b,c', a,b,c)
            B.append(1)
        else:
            #print('appending 0 in B: a,b,c', a,b,c)  
            B.append(0)
        i += 1
    return B

A = [1, 2, 2, 5, 5, 4]
res = validTriangle(A)
print(res)
