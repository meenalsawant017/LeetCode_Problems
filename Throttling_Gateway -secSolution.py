#https://leetcode.com/discuss/interview-question/819577/Throttling-Gateway-Hackerrank
import collections

def droppedRequests(requestTime):

        dropped = 0

        # you can include reqTime in enumerate for print purpose - debugging ( i.e., for i, reqTime in enumerate(requestTime) )
        for i, _  in enumerate(requestTime):
            if i > 2 and requestTime[i] == requestTime[i-3]:
                dropped += 1
                continue

            if i > 19 and requestTime[i] - requestTime[i-20] < 10:
                print('second if',i, " ", 'diff:',requestTime[i] - requestTime[i-20] ," ", requestTime[i],requestTime[i-20] )  
                dropped += 1
                continue

            if i > 59 and requestTime[i] - requestTime[i-60] < 60:
                print('second if',i, " ", 'diff:',requestTime[i] - requestTime[i-60] ," ", requestTime[i],requestTime[i-60] )  
                dropped += 1
        
        return dropped               
            
      

      
      
requestTime = [1,1,1,1,2] #1
#print(droppedRequests(requestTime))

requestTime = [1,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7,11,11,11,11] #7
print(droppedRequests(requestTime))

requestTime = [1,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7] #2
#print(droppedRequests(requestTime))
