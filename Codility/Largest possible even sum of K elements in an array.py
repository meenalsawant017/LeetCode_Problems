def largest_sum(arr, k):
      if len(arr) < k:
            return -1
      n = len(arr)
      arr.sort(reverse=True)
      i = 0
      stack = [(i, arr[0:i+k])]
      res = []
      

      while stack:
            start, sublist = stack.pop()
            total = sum(sublist)
            print('sublist:', sublist,'total', total)
            if total %2 ==0:
                  if sorted(sublist) not in res:
                        res.append(sorted(sublist))
                        return total
            else:
                  i += 1
                  sublist = arr[i:i+k]
                  stack.append([i,sublist])


#test case 1
arr = [4,9,8,2,6]
k = 3

#test case 2
arr = [5,6,3,4,2]
k = 5
print(largest_sum(arr,k))

#test case 2
arr = [10000]
k = 2
print(largest_sum(arr,k))

#test case 2
arr = [2,3,3,5,5]
k = 3
print(largest_sum(arr,k))
