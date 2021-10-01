def allLongestStrings(inputArray):
    h = {}
    
    for i in range(len(inputArray)):
        if len(inputArray[i]) not in h:
            h[len(inputArray[i])] = []
        h[len(inputArray[i])].append(inputArray[i])

    h = dict(sorted(h.items(), key=lambda x: x[0], reverse= True))

    for k,v in h.items():
        res = h[k]
        break
    
    return res

inputArray = ["aba", "aa", "ad", "vcd", "aba"]
print(allLongestStrings(inputArray))
    
