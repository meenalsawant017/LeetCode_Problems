def isMatch(str1, str2):
      h1 = {}
      string = 'abcdefghijklmnopqrstuvwxyz'
      s = set('{,},')
      stack = []
      newstr = ''

      for i in str1:
            if i not in h1:
                  h1[i] = 0
            h1[i] += 1

      for i in str2:
            if i not in string:
                  if i not in s:
                        stack.append(i)
            else:
                  while stack:
                        end = int(stack.pop())
                        start = int(stack.pop())
                        last_ele = newstr[-1]
                        if newstr in h1:
                              count = h1[newstr]
                              if count >= start and count < end:
                                    for j in range(1, count):
                                          newstr += last_ele
                              
                  newstr += i

                  
      if i == str2[-1] and stack != []:
            while stack:
                  end = int(stack.pop())
                  start = int(stack.pop())
                  last_ele = newstr[-1]
                  if newstr in h1:
                        count = h1[newstr]
                        if count >= start and count < end:
                              for j in range(1, count):
                                    newstr += last_ele
                        
                  
      if str1 == newstr:
            return True
      else:
            return False
                  
                  
print(isMatch("aa","a")) #→ false
print(isMatch("aa","aa")) #→ true
print(isMatch("aaa","aa")) #→ false
print(isMatch("aa","a{1,3}"))# → true
print(isMatch("aaa","a{1,3}")) #→ false
print(isMatch("ab","a{1,3}b{1,3}")) #→ true
print(isMatch("abc","a{1,3}b{1,3}c"))# → true
print(isMatch("abbc","a{1,3}b{1,2}c"))# → false
print(isMatch("acbac","a{1,3}b{1,3}c"))# → false
print(isMatch("abcc","a{1,3}b{1,3}cc{1,3}")) #→ true


