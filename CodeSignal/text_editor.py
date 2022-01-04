def solution(operations):
    #print(operations)
    clipboard = []
    cursor=0
    select_start = -1
    select_end = -1
    txt = []
    
    for line in operations:
        print(line)
        if(line.startswith("TYPE ")):
            txt_= (line[5:])
            
            if(select_start>=0 and select_end>=0):
                del txt[select_start:select_end+1]
                cursor=select_start
                
            for ele in txt_:
                txt.insert(cursor,ele)
                cursor+=1
            #cursor +=len(txt_)
            
            select_start = -1
            select_end = -1            
            
            print('txt', txt )
            print('cursor',cursor, 'len(txt)', len(txt))   
        elif(line.startswith("SELECT ")):
            sp = line.split(" ")
            select_start = int(sp[1])
            select_end = int(sp[2])
            cursor = select_end +1                      #removed +1 ASB
            print('select_start',select_start, 'select_end',select_end ,'cursor',cursor)
        elif(line.startswith("COPY")):
            if(select_start >=0 and  select_end >=0):
                clipboard.append("".join(txt[select_start:select_end+1]))
                print('clipboard', clipboard)
                
        elif(line.startswith("PASTE")):
            paste_idx = -1
            if(len(line) > 5):
                sp  = line.split(" ")
                paste_idx = -1 * int(sp[1])
            if(len(clipboard) < (paste_idx*-1)):
                continue
                
            print('paste_idx', paste_idx, 'clipboard_item', clipboard[paste_idx])
            #print('select_start',select_start, 'select_end',select_end ,'cursor',cursor)
            if(select_start>=0 and select_end>=0):
                del txt[select_start:select_end+1]
                cursor=select_start
                print('txt', txt , 'cursor',cursor)
            
            #txt[cursor:select_end] = (clipboard[paste_idx])
            
            pst = list(clipboard[paste_idx])
            for ele in pst:
                txt.insert(cursor,ele)
                cursor+=1
            #cursor = select_end+1
            print('txt', txt , 'cursor',cursor, 'len(txt)',len(txt) )
            
        elif(line.startswith("MOVE_CURSOR ")):
            select_start = -1
            select_end = -1
            sp  = line.split(" ")
            cursor += int(sp[1])
            #ASB ADDED below
            if(cursor < 0):
                cursor =0
            elif(cursor > len(txt)):
                cursor =len(txt)
            
            print('move cursor ', cursor)
        
    print("FINAL", ("".join(txt)))
      
    
'''oper = [
"TYPE Great Britain is the capital of London" ,
"SELECT 0 12",
"COPY",
"SELECT 32 37",
"COPY",
"PASTE 2",
"SELECT 0 12",
"PASTE",
"MOVE_CURSOR 32",
"TYPE !"
]

'''
'''
oper=[
'TYPE hello',
'SELECT 0 1',
'MOVE_CURSOR -1',
'TYPE world'
]
'''
'''
oper=[
'TYPE My dog',
'SELECT 3 4',
'MOVE_CURSOR -1', 
'TYPE ial',
'SELECT 0 1',
'TYPE His'
]

'''
'''
oper=[
'TYPE aba',
'SELECT 0 2',
'COPY',
'COPY',
'MOVE_CURSOR 1',
'TYPE c',
'PASTE 2'
]
'''
'''
oper=[
'COPY',
'TYPE hello',
'PASTE',
'SELECT 1 3',
'PASTE'
]
'''
'''
oper=[
'PASTE 1' ,
'PASTE 2',
'PASTE 3',
'COPY',
'PASTE 4',
'TYPE HEY'
]
'''
'''
oper=[
'TYPE verylongtext 123',
'MOVE_CURSOR -4',
'SELECT 5 8',
'TYPE AA',
'TYPE SUB'
]
'''
'''
oper=[
'TYPE verylongtext 456',
'MOVE_CURSOR -4',
'SELECT 8 13',
'TYPE AAAAAA',
'TYPE B'
]
'''
'''
oper=[
'TYPE verylongtext .?!',
'MOVE_CURSOR -4',
'SELECT 13 14',
'TYPE A',
'TYPE B'
]
'''
'''
oper=[
'TYPE Aba',
'MOVE_CURSOR -3',
'MOVE_CURSOR 10',
'TYPE AAA'
]
'''
'''
oper=[
'TYPE Aba',
'MOVE_CURSOR -10',
'TYPE AAA',
'SELECT 0 0',
'COPY'
]
'''
'''
oper=[
'TYPE HelloWorld',
'MOVE_CURSOR -2',
'TYPE aaa',
'MOVE_CURSOR -3',
'TYPE bbb',
]
'''
oper=[
'TYPE abc',
'SELECT 1 2',
'COPY',
'COPY',
'COPY',
'COPY',
'MOVE_CURSOR -3',
'PASTE 4',
'MOVE_CURSOR -10',
'PASTE'
]
solution(oper)
#London
#Great Britain
