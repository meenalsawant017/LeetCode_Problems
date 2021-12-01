def process(input_):
      cal_millisec = {}
      max_diff = 0
      res = []
      
      def totalmillisec(s):
            hh = int(s[0:2])
            mm = int(s[3:5])
            ss = int(s[6:8])
            time_millisec = hh*(3600) + mm*(60) + ss #+ ms
            return time_millisec
            
      print(input_)
      d ={}
      for i in range(len(input_)):
            ele = input_[i].split(",")
            source = ele[0].lstrip(" ")
            product = ele[1].lstrip(" ")
            quanity = ele[2].lstrip(" ")
            timestamp = ele[3].lstrip(" ")
            tmpstmp = totalmillisec(timestamp)
            if source == 'Exchange':
                  if product in d:
                        if quanity in d[product]:
                              val = d[product][quanity]
                              for i in val:
                                    diff = abs(i - tmpstmp)
                                    print('diff', diff)
                                    if diff > 300:
                                          return False
                              
                  
            if product not in d:
                  d[product] = {}
            if quanity not in d[product]:
                  d[product][quanity] = []
            d[product][quanity].append(tmpstmp) 
      return True    


input_ = ['Akuna, A, 10, 11:59:00', "Akuna, B, -15, 12:05:00",
          'Exchange, A, 10, 12:01:00',"Exchange, B, -15, 12:09:00"]

            
print(process(input_))
