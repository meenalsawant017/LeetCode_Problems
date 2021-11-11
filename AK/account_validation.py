#https://github.com/2208Abhinav/CodingInterviews/blob/master/Akuna%20Capital%20Junior%20Python%20Developer/images/Q11-AccountValidation.JPG
def process(line):
    num = int(line[0: 6], 16)
    '''
    try:
      num = int(line[0: 6], 16)
    except:
        print('except')  
        return "INVALID"
    '''
    num = int(line[0: 6], 16)
    summ = 0
    while num != 0:
        summ = summ + num % 10
        num = num // 10

    compare = hex(summ)[2:].upper()
    if line[6:] == compare:
        return "VALID"
    return "INVALID"


line = '8BADF00D'
print(process(line))
line = 'C0FFEE1C'
print(process(line))
