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

arr=[1,2,4,3]
pieces=[[1], [4,3], [2]]

arr=[1,2,4,3]
pieces=[[1], [3,4], [2]]
print(concatEdgeLetters(arr, pieces))
