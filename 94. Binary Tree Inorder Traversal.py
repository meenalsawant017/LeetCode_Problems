'''
94. Binary Tree Inorder Traversal

Input: root = [1,2,3,4,5,6,7]
Output: [4, 2, 5, 1, 6, 3, 7]

'''
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#class Solution:
def inorderTraversal(root: TreeNode):
      
      '''
      #Recursive method
      if root is None:
            return []
      else:
            return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right)
      '''
      
      # iterative method
      stack = []
      result = []
      while root is not None or stack != []:
            while root is not None:
                stack.append(root)
                root = root.left
            root = stack.pop()
            result.append(root.val)
            root = root.right
      return result
      

n = [1,2,3,4,5,6,7]
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

res = inorderTraversal(root)
print(res)
