import collections
def maximalNetworkRank(n, roads):

        indegree = collections.defaultdict(list)
        max_count = 0
        print(indegree)
        
        for u,v in roads:
            indegree[u].append(v)
            indegree[v].append(u)
        #print(indegree)
        
        for i in range(n):
            rank_i = len(indegree[i])
            for j in range(i+1, n):
                rank_j = len(indegree[j])
                if j in indegree[i]:
                    prev = max_count
                    max_count = max(max_count, rank_i + rank_j - 1)
                    if max_count > prev:
                        res = []
                        res.append([i, rank_i])
                        res.append([j, rank_j])
                else:
                    max_count = max(max_count, rank_i + rank_j)
                 
        #print('max_count',max_count)
        return max_count

n = 4
roads = [[0,1],[0,3],[1,2],[1,3]]
print(maximalNetworkRank(n, roads))
