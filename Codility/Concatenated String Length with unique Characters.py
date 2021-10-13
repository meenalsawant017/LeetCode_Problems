def max_length(arr):
      sorted_arr = sorted(arr)
      count = 0
      print('sorted_arr:',sorted_arr)
      for i in range(len(arr) - 1):
            if set(arr[i]) == set(arr[i+1]):
                  concat = arr[i] + arr[i+1]
                  print(concat)
                  count += 1
      return count
            
            



arr =  ["co","dil","ity"]
res = max_length(arr)
print(res)
