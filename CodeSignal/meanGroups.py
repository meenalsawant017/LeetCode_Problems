def meanGroups(a):
      h1 = {}

      for i in range(len(a)):
            arr = a[i]
            n = len(a[i])
            mean = sum(arr)/n
            if mean not in h1:
                  h1[mean] = []
            h1[mean].append(i)
      print('dict',h1)

      h1 = dict(sorted(h1.items(), key=lambda x: (x[1],x[0])))
      print(h1)

      ans = []
      for k,v in h1.items():
            ans.append(v)
      print(ans)
      return ans
      
a = [[3,3,4,2],
     [4,4],
     [4,0,3,3],
     [2,3],
     [3,3,3]]

print(meanGroups(a))
