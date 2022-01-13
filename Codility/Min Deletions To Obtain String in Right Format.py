'''
https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/

Min Deletions To Obtain String in Right Format

You are given a string s consisting only of characters 'X' and 'Y'.

Return the minimum number of deletions needed to make s balanced

'''
#Solution 1:

def minStep(s):
      charX = 'X'
      numY = 0
      minDel = 0
 
      for i in range(len(s)):
            if charX == s[i]:
                  minDel = min(numY, minDel + 1)
            else:
                  numY += 1
      return minDel



#Solution 2
'''
def minStep(s):

        # Data variables
        #Convert all the characters to list excluding the last one
        l = list(s[:-1]) 
        
        #Put the last character in stack
        stack = [s[-1]]
        
        #Counter to keep track of minimum deletions
        min_delete = 0
        
        #Iterate over the given string
        while l:
            
            #Pop the last element
            pop_item = l.pop()
            
            #Check if the top of the stack is 'a' and popped element is 'b'
            if stack and stack[-1] == 'X' and pop_item == 'Y':
                
                #Increament counter and remove element from stack
                min_delete += 1
                stack.pop()
                
                #Append that element into stack
            else:
                stack.append(pop_item)
        
        return min_delete
'''     
              
            
    
s = 'YXXXYXY' #2
#s = 'XXYYYY' #0
res = minStep(s)
print(res)
