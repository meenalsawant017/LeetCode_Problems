'''

40. Combination Sum II


Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[[1,1,6],
[1,2,5],
[1,7],
[2,6]]

Failed for this test case
candidates = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
Output: 27

'''

def combinationSum2(candidates, target):
        output = []
        def dfs(sublist, idx):
            total = sum(sublist)
                  
            if(total > target):
                return []
            
            if(total == target):
                  if(sorted(sublist) not in output):
                          output.append(sorted(sublist))
                          return             
                  
            for i in range(idx, len(candidates)):
                  sublist.append(candidates[i])
                  if(len(sublist) == len(candidates)):
                      if(sum(sublist) == target):
                            if(sorted(sublist) not in output):
                                  output.append(sorted(sublist))
                                  return
                                  break
                      else:
                            return
                  dfs(sublist, i+1)
                  sublist.pop()
                        
        dfs([],0)
        return output


'''
#candidates = [1,1,1,1,1,1,1,1]      
candidates = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
target = 27


#test case 2
candidates = [1]
target = 1


candidates = [1,1]
target = 2

'''
#test case 2
candidates = [10,1,2,7,6,1,5]
target = 8


res = combinationSum2(candidates, target)
print(res)
