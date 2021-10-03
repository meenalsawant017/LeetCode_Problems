import heapq
def canAttendFlight(intervals):
      intervals.sort()
      flights = 1
      heap = [intervals[0][1]]

      for start, end in intervals[1:]:
            if heap[0] <= start:
                  heapq.heappop(heap)
            else:
                  heapq.heappush(heap, end)
            flights = max(flights, len(heap))
      return flights

intervals = [[2,5], [3,7], [8,9], [7,10]]
print(canAttendFlight(intervals))



      
