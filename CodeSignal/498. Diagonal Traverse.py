import collections
def findDiagonalOrder(mat):
        R, C = len(mat), len(mat[0])
        diagonalDict = collections.defaultdict(list)

        for r in range(R):
            for c in range(C):
                diagonalDict[r+c].append(mat[r][c])
        print('diagonalDict:', diagonalDict)
        print("")
        
        
        ans = []
        for i, value in enumerate(diagonalDict.values()):
            if i % 2 == 0:
                ans += value[::-1]
            else:
                ans += value
        return ans
        
    
# Diagnal positions in top to bottom        
def dig_BottomToTop(mat):
        R, C = len(mat), len(mat[0])
        diagonalDict = collections.defaultdict(list)
        
        for r in range(R):
            for c in range(C):
                diagonalDict[r+c].append(mat[r][c])
        #print('diagonalDict:', diagonalDict)
        
        ans2 = []
        idx = 0
        for i, value in enumerate(diagonalDict.values()):
            ans2 += value[:]
            #print('Diagnal BottomToTop : ', ans2)
            
        new_mtx = [[0 for j in range(C)] for i in range(R)]
        
        for i in range(R):
            for j in range(C):
                new_mtx[i][j] = ans2[idx]
                idx += 1
        
        #print('Diagnal BottomToTop:', new_mtx)               
        return ans2

def dig_topToBottom(mat):
        R, C = len(mat), len(mat[0])
        diagonalDict = collections.defaultdict(list)
        
        for r in range(R):
            for c in range(C):
                diagonalDict[r+c].append(mat[r][c])
        #print('diagonalDict :', diagonalDict)
        
        ans2 = []
        idx = 0
        for i, value in enumerate(diagonalDict.values()):
            ans2 += value[::-1]
            #print('Diagnal topToBottom: ', ans2)
            
        new_mtx = [[0 for j in range(C)] for i in range(R)]
        
        for i in range(R):
            for j in range(C):
                new_mtx[i][j] = ans2[idx]
                idx += 1
        
        #print('Diagnal topToBottom:', new_mtx)        
                
        return ans2
      
matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]]

print('Zigzag: ',findDiagonalOrder(matrix))
print('BottomToTop: ',dig_BottomToTop(matrix))
print('topToBottom: ',dig_topToBottom(matrix))
