#https://algodaily.com/challenge_slides/matrix-operations/tests

'''
Can you write a method that returns the frequency of the max integer in the matrix? In the above example, it would be 1 (since 2 shows up just once).


1.Expect max_from_ops(4, 4, [[1, 1], [2, 2]]) to return 1
PYTHON
assert max_from_ops(4, 4, [[1, 1], [2, 2]]) == 1
Expect max_from_ops(4, 4, [[1, 1], [2, 2], [3, 3]]) to return 1
PYTHON
assert max_from_ops(4, 4, [[1, 1], [2, 2], [3, 3]]) == 1
Expect max_from_ops(4, 4, [[3, 3]]) to return 9
PYTHON
assert max_from_ops(4, 4, [[3, 3]]) == 9
RUN TESTS

'''

def max_from_ops(m, n, operations):
  
    min_col = m
    min_row = n

    for op in operations:
        min_col = min(min_col, op[0])
        min_row = min(min_row, op[1])
        print('min_row: ',min_row, 'min_col:', min_col)

    return min_col * min_row

#test case 1
m = 4
n = 4
operations = [[1, 1], [2, 2]]

#test case 2
m = 4
n = 4
operations = [[1,1], [3, 3]]
#operations = [[1, 1], [2, 2], [3, 3]]
print(max_from_ops(m, n, operations))

