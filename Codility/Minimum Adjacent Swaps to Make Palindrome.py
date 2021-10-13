'''
Minimum Adjacent Swaps to Make Palindrome
Given a string, what is the minimum number of adjacent swaps required to convert a string into a palindrome. If not possible, return -1.

Example 1:
Input: mamad
Output: 3
Explanation:
swap m with a => maamd

swap m with d => maadm

swap a with d => madam

Example 2:
Input: asflkj
Output: -1
Example 3:
Input: mideld
Output: 3
Explanation:
swap e with l => midled

swap e with d => midlde

swap l with d => middle

'''
# Approach 1
import collections
def min_swaps(s):
    def is_valid_palindrome(s: str) -> bool:
          count = collections.Counter(s)
          print('count', count)
          odd = 0
          for char, freq in count.items():
              if freq % 2 != 0:
                  odd += 1
          if odd <= 1:
              return True
          else:
              return False
          #OR
          #return len([char for char, freq in count.items() if freq % 2]) <= 1

    if not is_valid_palindrome(s):
        return -1

    # CONVERT TO LIST
    s = list(s)

    # SETUP FRONT BACK POINTER
    f, b = 0, len(s) - 1
    swaps = 0

    # LOOP TILL CROSS
    while f < b:

        # CASE 1 - FRONT = BACK
        if s[f] == s[b]:
            print('Case 1:', ' f: ', f, 'b: ', b)
            f += 1
            b -= 1
            

        # CASE 2 - FRONT != BACK
        else:

            # FIND THE RIGHTMOST CHAR TO MATCH THE FRONT
            mid = b
            while mid > f and s[f] != s[mid]:
                mid -= 1
            print('CASE 2','mid:', mid)

            # CASE 1 - CHAR NOT FOUND - SWAP ONCE WITH RIGHT NEIGHBOR, AND CONTINUE WITHOUT CLOSING WINDOW
            # THIS LONER CHAR WILL EVENTUALLY END UP IN THE MIDDLE OF THE STRING
            if mid == f:
                s[mid], s[mid + 1] = s[mid + 1], s[mid]
                swaps += 1
                print('CASE 2 --> CASE 1', 'swaps: ', swaps)
                continue

            # CASE 2 - CHAR FOUND - SWAP WITH RIGHT NEIGHBOR UNTIL IT ENDS UP AT THE BACK
            for i in range(mid, b):
                print('For loop', i)
                s[i], s[i + 1] = s[i + 1], s[i]
                swaps += 1
            
            # CLOSE THE WINDOW
            f += 1
            b -= 1

    return swaps




#s = 'mamad'
#print('Expected: ', 3, min_swaps(s))

#s = 'asflkj'
#print('Expected: ', -1, min_swaps(s))

#s = 'aabb'
#print('Expected: ', 2, min_swaps(s))

s = 'ntiin'
print('Expected: ', 1, min_swaps(s))
