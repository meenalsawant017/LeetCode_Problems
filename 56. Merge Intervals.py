'''
56. Merge Intervals

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

'''
def merge(intervals):
      intervals.sort(key = lambda pair: pair[0])
      output = [intervals[0]]

      for start, end in intervals:
            lastend = output[-1][1]
            if start <= lastend:
                 output[-1][1] = max(end , lastend) 
            else:
                  output.append([start, end])
      return output

intervals = [[1,3],[2,6],[8,10],[15,18]]
res = merge(intervals)
print(res)
