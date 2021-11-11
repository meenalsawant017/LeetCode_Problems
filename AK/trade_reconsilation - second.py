def process(input_):
      d = {}      
      output = []
      for i in range(len(input_)):
            line = input_[i]
            lst_str = line.split(",")

            if lst_str[0] == 'Reconsilation':
                  source1 = lst_str[1].lstrip(" ")
                  source2 = lst_str[2].lstrip(" ")
                  if source1 not in d:
                        output.append(0)
                        
                  elif source2 not in d:
                        output.append(len(d[source1]))
                  elif source1 and source2 in d:
                        count = 0
                        for i in d[source2]:
                              if i in d[source1]:
                                    count += 1
                        diff = len(d[source1]) - count
                        output.append(diff)
                  continue
            
            source = lst_str[0].lstrip(" ")
            product = lst_str[1].lstrip(" ")
            quanity = lst_str[2].lstrip(" ")
            timestamp = lst_str[3].lstrip(" ")                             
            temp = []
            temp = [product,quanity]
            
            tmp = " ".join(temp)
            if source not in d:
                  d[source] = []
            
            d[source].append(tmp)
            output.append(int(quanity))
            
      return output

input_ = ['Akuna, A, 10, 12:01:00', "Akuna, B, -15, 12:05:00", 'Reconsilation, Akuna, Exchange1',
          'Reconsilation,Exchange1, Akuna', "Exchange1,B, -15, 12:05:00", "Exchange1,B, -20, 12:05:00",
          'Reconsilation,Akuna, Exchange1','Reconsilation,Exchange1, Akuna', 'Reconsilation,Exchange2, Akuna']
print(process(input_))

#line = 'Reconsilation, Akuna, Exchange1'
#print(process(line))
