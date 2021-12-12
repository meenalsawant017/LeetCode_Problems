import math
def Rumble_Raffle(x,y,z):
      t = 0
      currPts = 0
      currRate = 2
      limit = int(z/x)

      for i in range(1, limit+1):
            reqTime = math.ceil((x-currPts)/currRate)
            leftPts =currPts + reqTime * (currRate)-x
            reqPts = z - leftPts
            print('reqTime:', reqTime, 'leftPts:',leftPts, 'reqPts:',reqPts)
            if reqTime + math.ceil((reqPts)/(currRate+y)) < math.ceil((z-currPts)/currRate):
                  print(math.ceil((z-currPts)/currRate))
                  t += reqTime
                  currPts = leftPts
                  currRate += y
            else:
                  break
      t += math.ceil((z-currPts)/currRate)
      return t      

print(Rumble_Raffle(500, 4, 2000))
      
