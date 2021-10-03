import collections
def findDiagonalOrder(mat):
        R, C = len(mat), len(mat[0])
        for i in range(R):
                for j in range(i+1, C):
                        if i==j:
                                continue
                        mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
        # Utility function to print a matrix
        def printMatrix(mat):
                for i in range(0, len(mat)):
                        for j in range(0, len(mat[0])):
                            print(mat[i][j], end="\t")
                        print('\n')
        printMatrix(mat)
                        
      
matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,11,12,12],
    [13,14,15,16]]

print(findDiagonalOrder(matrix))
