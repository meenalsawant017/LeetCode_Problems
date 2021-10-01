def prod(n):
      res = 1

      for i in range(len(n)):
            res *= int(n[i])
      return res

def add(n):
      res = 0

      for i in range(len(n)):
            res += int(n[i])
      return res

def result(n):

      production = prod(str(n))
      addition = add(str(n))

      res = production - addition
      print('prod: ', production, 'add: ',addition, 'res: ',res)
      return res

n = 123456
print(result(n))

            
