def CreateBoard(n):
      mtx = [ [ 0 for i in range(n) ] for j in range(n) ]

     
      #W = True
      
      for i in range(n):
            #W = not W
            for j in range(n):
                  print('i',i,'j',j,'i+j', (i+j)%2)
                  if ((i+j) % 2 )== 0:
                        print('WWWWW')
                        mtx[i][j] = 'W'
                  else:
                        mtx[i][j] = 'B'
            
      print(mtx)
            
                  


print(CreateBoard(2))
