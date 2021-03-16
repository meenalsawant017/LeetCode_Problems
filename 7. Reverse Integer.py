'''7. Reverse Integer
Example 1:

Input: x = 123
Output: 321
'''

def reverse(x):
    
        rev = 0
        if x == 0:
            rev = 0
        if x > 0:
            while(x > 0):
                a = x % 10
                rev = rev * 10 + a
                x = x // 10
            print('reverse integer' ,rev)
        #return rev
    
        if x < 0:
            x = -x
            while(x > 0):
                a = x % 10
                rev = rev * 10 + a
                x = x // 10
            rev = -1 * rev 
            
        if(pow(-2, 31) >= rev or rev >= pow(2, 31)):
              return 0
    
        else:
             return rev

num = 123
res = reverse(num)
