'''
max inserts to obtain string without 3 consecutive a
Given a string S, returns the maximum number of letters a that can be inserted into S
(including at the front and end of S) so that the resulting string doesn’t contain three
consecutive letters a. If string S already contains the substring aaa, then your function should return -1.

Example 1:
Input: aabab
Output: 3
Explanation:
A string aabaabaa can be made

Example 2:
Input: dog
Output: 8
Explanation:
A string aadaaoaagaa can be made

Example 3:
Input: aa
Output: 0
Explanation:
No longer string can be made.

Example 4:
Input: baaaa
Output: -1
Explanation:
There is a substring aaa


 If N is number of chars in the given string and all chars are not 'a' we can insert into this string 2 * (N + 1)
 chars because we can insert two As between of each two chars in the string and two As to the begin and
 to the end of the string.
 Thus in order to solve this task we need to count all non A chars. When we will know this number it will be easy
 to calculate how many As we can add. This number will be 2 * (number of possible places to insert + 1) - number of found As
 In other words 2 * (N + 1) - (N - number of As);
'''
def max_inserts(s):
      count = 0
      others = 0
      n = len(s)
      i = 0
      
      while i < n:
            if s[i] == 'a':
                  count += 1
                  
            else:
                  others += 1
                  count = 0

            if count == 3:
                  return -1
            i += 1

      return  2 * (others + 1) - (n - others)

s = 'aabab' # 3
print(max_inserts(s))
s = 'dog' # 8
print(max_inserts(s))
s = 'aa' # 0
print(max_inserts(s))
s = 'baaaa' # -1
print(max_inserts(s))





'''
def max_inserts(s):
      stack = []
      ch = 0
      insertCount = 0
      counter = 0

      while ch < len(s):
            if s[ch] == 'a':
                  print('first if',s[ch])
                  counter += 1
                  stack.append(s[ch])
                  ch += 1
                  if counter > 2:
                        return -1
            elif(s[ch] != 'a' and counter < 2):
                  print('second if',s[ch])
                  stack.append('a')
                  insertCount += 1
                  counter += 1
                  #ch -= 1
            elif(s[ch] != 'a' and counter >= 2):
                  print('third if',s[ch])
                  stack.append(s[ch])
                  counter = 0
                  ch += 1

      #result = ''.join(stack)
      
      if stack[-1] != 'a' :
            stack.append('aa')
            insertCount += 2
      if stack[-1] == 'a' and counter < 2:
            stack.append('a')
            insertCount+=1
  #dogaa
      print('stack:', ''.join(stack))      
      return insertCount

'''
