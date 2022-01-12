'''
Solution: To solve this task we need to find sequences of the same letters and
if the sequence is longer than 3 divide length of this sequence to 3 and add
result of the division to counters of needed moves.

'''

def min_moves(s):
      res = 0
      size = len(s)
      i = 0

      while i < (size):
            next_ = i + 1
            while (next_ < size) and s[i] == s[next_]:
                  #print('i', i, 'next_', next_)
                  next_ += 1
            #print('next_', next_, i)
            res += (next_ - i)//3
            i = next_
      return res


s = 'baaaaa' #1
print(min_moves(s))

s = 'baaabbaabbba' #2
print(min_moves(s))

s = 'baabab' #0
print(min_moves(s))

