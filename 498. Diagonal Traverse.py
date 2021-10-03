import collections
def findDiagonalOrder(mat):
        R, C = len(mat), len(mat[0])
        diagonalDict = collections.defaultdict(list)
		# key - diagonal elements have the same r + c value.
        for r in range(R):
            for c in range(C):
                diagonalDict[r+c].append(mat[r][c])
        print('diagonalDict:', diagonalDict)
        
        '''
        ans = []
        for i, value in enumerate(diagonalDict.values()):
            if i % 2 == 0:
                ans += value[::-1]
            else:
                ans += value
        #return ans
        '''
    
        # Diagnal positions
        ans2 = []
        idx = 0
        for i, value in enumerate(diagonalDict.values()):
            ans2 += value[::-1]
            print('Diagnal positions: ', ans2)
            
        new_mtx = [[0 for j in range(C)] for i in range(R)]
        
        for i in range(R):
            for j in range(C):
                new_mtx[i][j] = ans2[idx]
                idx += 1
        
        print('new_mtx:', new_mtx)        
                
        return ans2
      
matrix = [
    [1,2,2,3],
    [3,4,10,4],
    [2,10,1,2],
    [5,4,4,5]]

print(findDiagonalOrder(matrix))
