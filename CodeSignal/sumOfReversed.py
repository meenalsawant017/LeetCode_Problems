def rev_add(arr):
      def rev(num):
            count = 0
            reversed_num = 0
            while num != 0:
                  if num% 10 == 0:
                        count += 1
                  digit = num % 10
                  reversed_num = reversed_num * 10 + digit
                  num //= 10
            for i in range(count):
                  reversed_num =  str(reversed_num) + '0'
            return int(reversed_num)

      new_arr =[]
      for i in arr:
            reversed_num = rev(i)
            new_arr.append(reversed_num)
      return sum(new_arr)

arr = [7, 234, 58100]
print(rev_add(arr))

