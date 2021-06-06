def rotate_withoutdiagonals(matrix):
        n = len(matrix[0])
        # find all the diagonal positions
        diag = [ (i,i) for i in range(0,len(matrix)) ]
        reverseDiag = [ (2,0), (1,1), (0,2)]

        for i in range(n):
            for j in range(i,n):
                if (i,j) in diag or (i,j) in reverseDiag:
                    continue
                else:
                    matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
        # reverse the middle row
        matrix[1].reverse()
        
        return matrix
'''matrix = [
    [1,2,2,3],
    [3,4,10,4],
    [2,10,1,2],
    [5,4,4,5],
]'''
matrix = [[1, 2, 3, 4, 5],
[6, 7, 8, 9, 10],
[11, 12, 13, 14, 15],
[16, 17, 18, 19, 20],
[21, 22, 23, 24, 25]]

res = rotate_withoutdiagonals(matrix)
print(res)
