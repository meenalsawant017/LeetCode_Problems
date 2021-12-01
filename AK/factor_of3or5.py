def isFactor(l, r):

      def isIdeal(n):
            while n % 3 == 0:
                  n /= 3
            while n % 5 == 0:
                  n /= 5
            return n == 1

      i = l
      count = 0 
      while i <= r:
            if isIdeal(i):
                  count += 1
            i += 1
      return count
            

print(isFactor(200, 405))
