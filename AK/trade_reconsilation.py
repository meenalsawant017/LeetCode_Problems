def process(input_):
      print(input_)
      d ={}
      output = []
      for i in range(len(input_)):
            d2 = {}
            ele = input_[i].split(",")
            source = ele[0].lstrip(" ")
      
            if source == 'Reconsilation':
                  count = 0
                  company1 = ele[1].lstrip(" ")
                  counterparty = ele[2].lstrip(" ")
                  if company1 not in d:
                        output.append(0)
                        continue
                  tmp = 0
                  if counterparty in d:
                        for k,v in d[company1].items():
                              count = 0
                              if k in d[counterparty]:
                                    for i in range(len(d[company1][k])):
                                          for j in range(len(d[counterparty][k])):
                                                if d[company1][k][i] == d[counterparty][k][j]:
                                                      count += 1
                              tmp += len(v) - count
                        output.append(tmp)
                  else:
                        output.append(len(d[company1]))

                  continue
                              
            product = ele[1].lstrip(" ")
            quanity = ele[2].lstrip(" ")
            timestamp = ele[3].lstrip(" ")
            
            output.append(quanity)
            if source not in d:
                  d[source] = {}
            if product not in d[source]:
                  d[source][product] = []
            d[source][product].append([quanity, timestamp]) 
      return output      
      '''
      d1= {"A" : [[10,"12:05"]]}
      
      d1["B"] = [[20,"12:06"]]
      d1["B"].append([30,"12:10"])
      print(d1)
      d["AKUNA"]= d1
      print(d)
      print(d["AKUNA"]["B"])

      '''

input_ = ['Akuna, A, 10, 12:01:00', "Akuna, B, -15, 12:05:00", 'Reconsilation, Akuna, Exchange1',
          'Reconsilation,Exchange1, Akuna', "Exchange1,B, -15, 12:05:00", "Exchange1,B, -20, 12:07:00",
          'Reconsilation,Akuna, Exchange1','Reconsilation,Exchange1, Akuna', 'Reconsilation,Exchange2, Akuna']

            
print(process(input_))
