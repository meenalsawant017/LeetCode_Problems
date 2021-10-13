'''

Day of week that is K days later

https://algo.monster/problems/day_of_week

Given current day as day of the week and an integer K, the task is to find the day of the week after K days.

Example 1:
Input:
day = “Monday”

K = 3

Output: Thursday

'''

def dayOfWeek(day, k):
      day_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

      for d in range(len(day_list)):
            if day_list[d] == day:
                  idx = d
                  ans =(idx + k) % 7
                  if ans == 0:
                        res = day
                  else:
                        res = day_list[ans]
      return res
      print(ans)

day = "Monday"
k = 3

res = dayOfWeek(day, k)
print(res)
