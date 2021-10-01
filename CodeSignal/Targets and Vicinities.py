#Targets and Vicinities
'''
Notice that both the actual number and the guess have the same values, in the same position, with regards to 3 and 4.

Now onto "vicinities". Vicinities are digits in guess that have the same value as some digit in actual, but don't share the same position (hence the nomenclature).

Person 1 has to tell person 2 how many targets and vicinities there are by providing a string in this format:


'''

def getTV(actual, guess):
    h1 = {}
    h2 = {}
    res_t = 0
    res_v = 0
    
    for i in range(len(actual)):
        h1[actual[i]] = i
    
    for k,v in h1.items():
      if k == guess[v]:
        res_t += 1
      
    for v in range(len(guess)):
        if guess[v] in h1:
          if v != h1[guess[v]]:
            res_v += 1
    return str(res_t) + 'T' + str(res_v) + 'V'


print(getTV('345', '135'))# == '1T1V'
print(getTV('01', '01')) #== '2T0V'
print(getTV('130', '893'))# == '0T1V'



      

