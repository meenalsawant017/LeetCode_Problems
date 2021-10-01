#https://leetcode.com/discuss/interview-question/933426/OA-Uber
def hashMap(queryType, query):
    d,s,c1,c2={},0,0,0
    for i,j in zip(queryType,query):
        if i == 'insert':
            d[j[0]-c1]=j[1] - c2
        elif i == 'addToValue':
            c2+=j[0] 
        elif i == 'addToKey':
            c1+=j[0] 
        elif i== 'get':
            s+=d[j[0]-c1]+c2 
    return s

queryType=["insert","insert","addToValue","addToKey","get"]
query=[[1,2],[2,3],[2],[1],[3]]
print('hashMap(queryType, query):', hashMap(queryType, query))
