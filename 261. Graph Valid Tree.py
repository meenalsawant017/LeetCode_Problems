def validTree(n, edges):
      if not n:
            return True
      
      adjlist = {i:[] for i in range(5)}
      visit = set()
      prev = None

      for i, j in edges:
            adjlist[i].append(j)
            adjlist[j].append(i)

      print(adjlist)
      def dfs(i, prev):
            if i in visit:
                  return False
            
            visit.add(i)
            for j in adjlist[i]:
                  if j == prev:
                        continue
                  if not dfs(j, i):
                        return False
            return True
      return dfs(0, -1) and len(visit) == n
      
      

n = 5
edges = [[0,1], [0,2], [0,3], [1,4]]
print(validTree(n, edges))
