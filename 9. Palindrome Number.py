'''
9. Palindrome Number
Example 1:

Input: x = 121
Output: true


'''
def isPalindrome(x):
        temp = x
        if type(x) is int:
            rev = 0
            while (x> 0):
                a = x % 10
                rev = rev * 10 + a
                x = x//10
        
        if (temp == rev):
            #print('x is equal to rev')
            return True
        if(pow(-2, 31) >= rev or rev >= pow(2, 31)):
            #print('x is not equal to rev')
            return False
        if(temp < 0):
            #print('x is not equal to rev')
            return False

x = 121
res = isPalindrome(x)
print(res)
