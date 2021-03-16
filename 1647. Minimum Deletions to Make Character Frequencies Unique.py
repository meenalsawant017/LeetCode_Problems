'''
1647. Minimum Deletions to Make Character Frequencies Unique

Example 1:

Input: s = "aab"
Output: 0
Explanation: s is already good.

Example 2:

Input: s = "aaabbbcc"
Output: 2
Explanation: You can delete two 'b's resulting in the good string "aaabcc".
Another way it to delete one 'b' and one 'c' resulting in the good string "aaabbc".
Example 3:

Input: s = "ceabaacb"
Output: 2
Explanation: You can delete both 'c's resulting in the good string "eabaab".
Note that we only care about characters that are still in the string at the end
(i.e. frequency of 0 is ignored).
'''

from collections import Counter 
def minDeletions(s):
        mylist = list(collections.Counter(s).values())

        s_set = set()
        
        counter = 0
        for i in mylist:
            while i in s_set:
                i -= 1
                counter += 1
            if i > 0 :
                s_set.add(i)
        return counter

s = "aab"
res = minDeletions(s)
print(res)
    
        
