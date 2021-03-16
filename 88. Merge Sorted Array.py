'''
88. Merge Sorted Array

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]


'''
def merge(nums1, m, nums2, n):
      #nums1 = nums1[:m]
      #nums2 = nums2[:n]
      length = m + n
      
      
      #for i in range(m+1, length):
      i = m
      for j in range(n):
            nums1[i] = nums2[j]
            if(i < length):
                  i += 1 
      nums1.sort()
      print(nums1)
      


nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

res = merge(nums1, m, nums2, n)

