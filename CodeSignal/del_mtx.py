def del_matrix(matrix, r, c):
      row = len(matrix)
      col = len(matrix[0])
      tmp_list = []
      new_mtx = []   
      
      for i in range(row):
            if i == r:
                  continue
            else:
                  tmp = matrix[i]
                  new_mtx.append(tmp)
      print('row: new_mtx-->',new_mtx)

      for i in range(len(new_mtx)):
            for j in range(col):
                  if j == c:
                        del new_mtx[i][j]
                  
      print('col: new_mtx-->',new_mtx)
      return new_mtx
                  

matrix = [
    [1,2,2,3],
    [3,4,10,4],
    [2,10,1,2],
    [5,4,4,5],
]

print(del_matrix(matrix, 0, 2))
