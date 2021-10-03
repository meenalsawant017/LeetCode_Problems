def mutateTheArray(n, a):
    return [a[0]+a[1]]+[sum(a[x-1:x+2])for x in range(1,len(a))]if n>1 else a

'''
Given an array of positive integers a, your task is to calculate the sum
of every possible a[i] ∘ a[j], where a[i] ∘ a[j] is the concatenation
of the string representations of a[i] and a[j] respectively.
'''
def concatenationsSum(a):
      total = 0

      for i in range(len(a)):
            for j in range(len(a)):
                  new = str(a[i]) + str(a[j])
                  total += int(new)
      return total

def concatenationsSum(a):
    t=sum(a)
    t1=t*len(a)
    t2=sum([t*[len(str(x))-1 for x in a].count(j)*10**(j+1) for j in range(7)])
    return t1+t2

def countTinyPairs(a, b, k):
      pair = set()
      for i in range(len(a)):
            j = len(b) - i - 1
            tmp = ''
            tmp = str(a[i]) + str(b[i])
            if int(tmp) < k:
                  if tmp not in pair:
                        pair.add(tmp)
      return len(pair)

def mergeStrings(s1, s2):
    s,o1,o2='',s1,s2
    while len(s1)*len(s2)!=0:
        if o1.count(s1[0])>o2.count(s2[0]) or (o1.count(s1[0])==o2.count(s2[0]) and s1[0]>s2[0]):
            print('if')  
            s+=s2[0]
            s2=s2[1:]
        else:
            s+=s1[0]
            s1=s1[1:]
    return s+s1+s2

#For queryType=["insert","insert","addToValue","addToKey","get"]
#and query=[[1,2],[2,3],[2],[1],[3]], the output should be hashMap(queryType,query)=5.

def hashMap(queryType, query):
    d,s,c1,c2={},0,0,0
    for i,j in zip(queryType,query):
        if i == 'insert':
            d[j[0]-c1]=j[1] - c2
        elif i == 'addToValue':
            c2+=j[0] #2
        elif i == 'addToKey':
            c1+=j[0] #1
        elif i== 'get':
            s+=d[j[0]-c1]+c2 # d[2-1] + 2 =d[1] + 2
    return s

def mostFrequentDigits(n):
      n = int(n)
      h = {}

      while n > 0:
            digit = n % 10
            if digit not in h:
                  h[digit]  = 0
            h[digit] += 1
            n = n//10
      print('mostFrequentDigits', h)
      
    

def alternatesort(a):
      a.sort(reverse=True)
      i = 0
      j = len(a)-1
      res = []

      while i<j:
            res.append(a[i])
            res.append(a[j])
            i += 1
            j -= 1
      if i == j:
            res.append(i)
      if i > j:
            return res
            
                              
print('mutateTheArray-->',mutateTheArray(5,[4, 0, 1, -2, 3]))

a = [10, 2]
print('concatenationsSum-- >',concatenationsSum(a))

#test case 1
a = [2, 9, 2]
b = [5, 3, 5]
k = 30

#test case 2
a = [1,2,3,4,5]
b = [1,2,3,4,5]
k = 40
print('countTinyPairs->',countTinyPairs(a, b, k))
print('mergeStrings->', mergeStrings('abade', 'bbde'))

queryType=["insert","insert","addToValue","addToKey","insert","get"]
query=[[1,2],[2,3],[2],[1], [3,6],[3]]
print('hashMap(queryType, query):', hashMap(queryType, query))
print(mostFrequentDigits('12345612'))
print('alternatesort(a)',alternatesort([2,1,4,6,8,3,7,9,10]))
