def max_length(arr):
        maxlen = 0
        unique = ['']
        
        def isValid(s):
            if len(s) == len(set(s)):
                return True
            
        
        for word in arr:
            print('word:', word)
            for j in unique:
                print('j:', j)
                tmp = word + j
                if isValid(tmp):
                    #if(tmp not in unique):
                    unique.append(tmp)
                    #print('Appending...', unique)
                    maxlen = max(maxlen, len(tmp))
                    
        return maxlen
            
            



arr =  ["co","dil","ity"]
res = max_length(arr)
print(res)
