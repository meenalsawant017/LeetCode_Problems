#https://leetcode.com/discuss/interview-question/819577/Throttling-Gateway-Hackerrank
import collections

def dropRequest(requestTime):
      
      drop = 0
      d = dict(collections.Counter(requestTime))
      d = (sorted(d.items()))
      print('d: ->', d)
      
      TxNum1= 0   #3
      TxNum10= 0  #20
      TxNum60= 0  #60
      
      allowedTx1sec =3
      allowedTx10sec = 20
      allowedTx60sec = 60
      
      dropped =0
      
      for i, n in enumerate(d):
            print(i,n)
            time = d[i][0]
            tx = d[i][1]
            
            
            TxNum1 = tx
            TxNum10 += tx
            TxNum60 += tx

            if(time > 10):
                  index2minus = 10 - (i + ((time -i)-1))
                  TxNum10 -= d[index2minus][1]
                  print('window 10 , index ',index2minus ,'val ', d[index2minus][1] )

            if(time > 60):
                  index2minus = 60 - (i + ((time -i)-1))
                  TxNum60 -= d[index2minus][1]
                  print('window 60 , index ',index2minus ,'val ', d[index2minus][1] )

            if( TxNum1 > allowedTx1sec):
                  dropped += TxNum1-allowedTx1sec
                  
            if( TxNum10 > allowedTx10sec):
                  dropped += TxNum10-allowedTx10sec

            if( TxNum60 > allowedTx60sec):
                  dropped += TxNum10-allowedTx60sec                  
            
      return dropped

      
      

requestTime = [1,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,7,7,7,7,11,11,11,11]
print(dropRequest(requestTime))
