'''

String Without 3 Identical Consecutive Letters

Given a string S having lowercase English letters,
returns a string with no instances of three identical consecutive letters,

obtained from S by deleting the minimum possible number of letters.

Example 1:
Input: eedaaad
Output: eedaad
Explanation:
One occurrence of letter a is deleted.

Example 2:
Input: xxxtxxx
Output: xxtxx
Explanation:
Note that letter x can occur more than three times in the returned string
if the occurrences are not consecutive.

Example 3:
Input: uuuuxaaaaxum
Output: uuxaaxum

0123456
xxxtxxx
    i j

x==x
counter = 13
str[i:j]

'''

def filter_string(s):
      i = 0
      j = 1
      counter = 0
      while i <= j :
            if s[i] == s[j]:
                  counter += 1
                  if counter >= 2:
                        s = s[:j] + s[j+1:]
                        i = j-1
                        j = j-1
            elif(s[i] != s[j]):
                  counter = 0
                  i = j
            if j < len(s)-1:
                  j += 1
            else:
                  return s

def filter_string2(s):
    news = s[0:2]
    #return ''
    for i in range(2, len(s)):
        # Do not append if the previous chars are the same
        if s[i] != s[i - 1] or s[i] != s[i - 2]:
            news += s[i]
    return news

#s = 'eedaaad'
#s = 'xxxtxxx'
s = 'uuuuxaaaaxum'
#s = 'abaaaa'
res = filter_string(s)
print('ans',res)

#res2 = filter_string2(s)
#print(res2)
