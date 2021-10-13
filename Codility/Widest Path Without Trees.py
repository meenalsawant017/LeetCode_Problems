'''

Widest Path Without Trees

There are N trees (numbered from 0 to N-1) in a forest.
The K-th tree is located at coordinates (X[K], Y[K]).
We want to build the widest possible vertical path,
such that there is no tree on it. The path must be
built somewhere between a leftmost and a rightmost tree,
which means that the width of the path cannot be infinite.

Example 1:
Input: X = [5,5,5,7,7,7], Y=[3,4,5,1,3,7]

Output: 2

Example 2:
Input: X = [6,10,1,4,3], Y=[2,5,3,1,6]

Output: 4

Example 3:
Input: X = [4,1,5,4], Y=[4,5,1,3]

Output: 3

'''

def widest_path(x, y):
      difference = 0
      sorted_x = sorted(x)

      for i in range(0, len(sorted_x) - 1):
            diff = sorted_x[i+1] - sorted_x[i]
            if diff > difference:
                  difference = diff
      return difference



#X = [5,5,5,7,7,7]
#Y=[3,4,5,1,3,7]

#X = [6,10,1,4,3]
#Y=[2,5,3,1,6]

X= [4,1,5,4]
Y=[4,5,1,3]

res = widest_path(X, Y)
print(res)
