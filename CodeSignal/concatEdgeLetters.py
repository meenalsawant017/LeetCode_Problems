#https://leetcode.com/discuss/interview-question/851434/one-codesignal-oa-question
'''
Given a target list arr and a list of pieces pieces, check if we can concatenate the items in pieces to form arr.

Example 1: arr=[1,2,4,3], pieces=[[1], [4,3], [2]] > True
Example 2: arr=[1,2,4,3], pieces=[[1], [2], [3, 4]] > False


'''
def concatEdgeLetters(arr, pieces):
      mapping = {k[0]: k for k in pieces }
      print(mapping)
      ans = []
      
      for a in arr:
            if a in mapping:
                  ans.extend(mapping[a])
      return True if arr == ans else False

#Approach 2
from collections import deque
def canFormArray(arr, pieces):
      hmap = {arr[a]:a for a in range(len(arr))}
      for i in range(len(pieces)):
            if len(pieces[i])>1:
                  for k in range(len(pieces[i])-1):
                        if pieces[i][k] not in hmap or pieces[i][k+1] not in hmap:
                              return False
                        if hmap[pieces[i][k+1]]-hmap[pieces[i][k]]>1 or hmap[pieces[i][k]]>hmap[pieces[i][k+1]]:
                              return False
            else:
                if pieces[i][0] not in hmap:
                    return False
      return True

arr=[1,2,4,3]
pieces=[[1], [4,3], [2]]
print(concatEdgeLetters(arr, pieces))
print(canFormArray(arr, pieces))


arr=[1,2,4,3]
pieces=[[1], [3,4], [2]]
print(concatEdgeLetters(arr, pieces))
print(canFormArray(arr, pieces))
