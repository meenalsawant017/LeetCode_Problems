import collections
def zigzag(arr):
      d = {}
      res = []
      
      ROW = len(arr)
      COL = len(arr[0])

      for i in range(ROW):
            for j in range(COL):
                  if arr[i][j] not in d:
                        d[arr[i][j]]  = 0
                  
                  d[arr[i][j]]+= 1
      d = dict(sorted(d.items(), key = lambda x:[x[1],x[0]], reverse = True))    
      
      for k,v in d.items():
            for i in range(v):
                  res.append(k)
      

      new_mtx = [[0 for i in range(COL)] for i in range(ROW)]
      idx = 0
      
      print(new_mtx)
      print('res:', res)
      
      '''for line in range(1, (ROW + COL)):
            start_col = max(0, line - ROW)
            count = min(line, (COL - start_col), ROW)
            
            for j in range(0, count):
                  #print(min(ROW, line) - j - 1,start_col + j,"-->",matrix[min(ROW, line) - j - 1]
                  #      [start_col + j], end="\t")
                  new_mtx[min(ROW, line) - j - 1][start_col + j] = res[idx]
                  idx += 1
      return new_mtx
      ''' 
      
      R, C = len(arr), len(arr[0])
      diagonalDict = collections.defaultdict(list)
		# key - diagonal elements have the same r + c value.
      for r in range(R):
            for c in range(C):
                  diagonalDict[r+c].append(res[idx])
                  idx += 1
      print('diagonalDict', diagonalDict)
      ans  = []
      #for i, value in enumerate(diagonalDict.values()):
            

                  
        
     
# Utility function to print a matrix
def printMatrix(matrix):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            print(matrix[i][j], end="\t")
        print('\n')
 



matrix = [[3,-2,4],
          [3,-2,1],
          [4,3,1]]
printMatrix(matrix)

print('zigzag--->')
res = zigzag(matrix)
print(res)
#printMatrix(res)
