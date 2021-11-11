def outage_interval(trade_data):
      cal_millisec = {}
      max_diff = 0
      res = []
      
      def totalmillisec(s):
      
            hh = int(s[0:2])
            mm = int(s[3:5])
            ss = int(s[6:8])
            ms = int(s[9:11])
            cal = hh*(3600*1000) + mm*(60*1000) + ss*1000 + ms
            print(cal)
            
            cal_millisec[s]= cal
            
      
      for s in trade_data:
            totalmillisec(s)

      cal_millisec = sorted(cal_millisec.items(), key = lambda x:x[1])
      print(cal_millisec)

      for i in range(1,len(cal_millisec)):
            diff = cal_millisec[i][1] - cal_millisec[i-1][1]
            if max_diff < diff:
                  max_diff = diff
                  print('MAX', max_diff, )
                  res = [[cal_millisec[i-1][0]],[cal_millisec[i][0]]]
      return res    
            

trade_data = ["12:31:16:98", "12:31:05:01", "12:31:04:04", "12:31:06:21", "12:31:14:39", "12:31:15:13", "12:31:17:89"]
print(outage_interval(trade_data))
