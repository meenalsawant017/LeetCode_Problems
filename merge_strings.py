"""
Given two strings a and b, merge the strings so that the letters are added in alternating order
starting with string a. If one string is longer than the other, then append the letters to the end of the merged string.
ex. "abcd", "efghi" -> "aebfcgdhi"
ex. "", "abcd" -> "abcd"
ex. "abcdefg", "zxy" -> "azbxycdefg"
"""

a ='abcd'
b = 'efghi'

def mergeStrings(a,b):
    res = ''
    print(list(zip(a,b)))
    for l1,l2 in zip(a,b):
        res += l1 + l2
    if len(a) < len(b):
        res += b[len(a):]
    elif len(a) > len(b):
        res += a[len(b):]
    return res

print(mergeStrings(a,b)) # aebfcgdhi
