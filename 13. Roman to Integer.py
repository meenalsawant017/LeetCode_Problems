'''
13. Roman to Integer

Example 1:

Input: s = "III"
Output: 3

'''

def romanToInt(s):
        S = s.upper()
        list_roman_num = {
            "I": 1, 
            "V": 5, 
            "X": 10, 
            "L": 50, 
            "C": 100, 
            "D": 500, 
            "M": 1000
        }
        
        temp_total = 0
        i = 0
        
        while (i < len(S)-1):  
            if(list_roman_num[S[i]] >= list_roman_num[S[i+1]]):
                temp_total += list_roman_num[S[i]] 
                i += 1
            else:
                temp_total = temp_total + (list_roman_num[S[i+1]] - list_roman_num[S[i]]) 
                i += 2
        
        if (i < len(S)):
            temp_total = temp_total + list_roman_num[S[i]]
            
        #print('Final Total',temp_total)
        return temp_total

s = 'III'
res = romanToInt(s)
print(res)
