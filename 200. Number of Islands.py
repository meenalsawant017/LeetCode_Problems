'''
200. Number of Islands

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

'''

def numIslands(grid):
        if not grid:
            return 0;

        row= len(grid)
        col=len(grid[0])
        stack = []
        count = 0
        
        for i  in range(row):
            for j in range(col):
                print(grid[i][j], end=' ')
            print("")
        print("")
                
                
        for x  in range(row):
            for y in range(col):
                if(grid[x][y] == '1'):
                    count += 1
                    stack.append([x,y])
                    while(stack):
                        i,j = stack.pop()
                        
                        if grid[i][j] == '1':
                            grid[i][j] = 'X'
                        
                        #Down
                        if  i + 1 < row and grid[i + 1][j] == '1':
                            stack.append([i + 1, j])
                        
                        #Right
                        if  j + 1 < col and grid[i][j+1] == '1':
                            stack.append([i, j+1])
                        
                        #Up
                        if i - 1 >= 0 and grid[i- 1][j] == '1':
                            stack.append([i - 1, j])
                            
                        #left
                        if j - 1 >= 0 and grid[i][j - 1] == '1':
                            stack.append([i, j - 1])
        return count
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
      
res = numIslands(grid)
print('Output',res)
