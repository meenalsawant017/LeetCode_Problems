#https://stackoverflow.com/questions/56373582/how-can-i-count-how-many-horizontal-brush-strokes-are-required-to-draw-an-array

def countBrushSTrokes(arr):

      count = 0
      prev = 0

      for i in range(len(arr)):
            print('arr[i]:', arr[i], 'prev:', prev, 'count', count)
            if (arr[i] > prev):
                  count = count + (arr[i] - prev)
                  print('diff', arr[i]-prev)
            prev = arr[i]
      return count

arr = [1,4,3,2,3,1]
print(countBrushSTrokes(arr))
