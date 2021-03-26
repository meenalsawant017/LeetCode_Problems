def missing(horizontalCuts, n):
      interval = []
      for i in range(len(horizontalCuts)):
            x = horizontalCuts[i] - 1
            y = horizontalCuts[i] + 1
            if(x >= 0):
                  interval.append(x)
            if(y <= n):
                  interval.append(y)

      min_val = min(interval)
      max_val = max(interval)

      hcuts = [min_val,max_val]
      print('cuts',hcuts)
      return hcuts


def maxArea( h, w, horizontalCuts, verticalCuts):
        h = h + 1
        w = w + 1
        #print('h',h,'w',w)
        h_interval = missing(horizontalCuts, h)
        v_interval = missing(verticalCuts, w)
        print('h_interval',h_interval,'v_interval',v_interval)
        h_diff = max(h_interval)- min(h_interval)
        v_diff = max(v_interval) - min(v_interval)
        result = h_diff * v_diff *1 
        print('result',result)
        
'''n = 5
m = 4
h = [1,2,4]
v = [1,3]'''


#test case 1
n = 6
m = 6
h = [4]
v = [2]


#test case 2
n = 3
m = 3
h = [2]
v = [2]


#test case 3
n = 4
m = 3
h = [1, 2, 3]
v = [1, 2]


res = maxArea(n, m, h, v)
print(res)
