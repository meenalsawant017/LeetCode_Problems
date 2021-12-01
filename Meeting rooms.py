def canAttendMeetings(arr):
      arr.sort()
      lastend = -1
      for start, end in arr:
            if lastend <= start:
                  lastend = end
            else:
                  return False
      return True


arr = [[0,30],[5,10],[15,20]]
print(canAttendMeetings(arr))

arr = [[7,10],[2,4]]
print(canAttendMeetings(arr))
