from collections import Counter
n = 5
res=0
#a=[4,8,2,8,9,8,8,4]
a = [4,8,2,8,9]
ct=Counter(a)
print(ct)
for i in ct:
      if ct[i]%2!=0:
            print(ct[i])
            res+=1
print(res)

