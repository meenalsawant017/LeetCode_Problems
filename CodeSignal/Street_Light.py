def streetLights(n, lights):
        new_list = []

        for i,j in lights:
                start = i-j
                end = i+j
                new_list.append([start,end])
                
        new_list.sort()

        output = [new_list[0]]

        for start, end in new_list[1:]:
                lastend = output[-1][1]
                if lastend <= start:
                        output.append([start, end])

        if (output[0][0]<= 0 and output[-1][1] >= n):
                return len(output)
        else:
                return -1
        
        

n = 10
#lights = [[-5, 5], [-2, 4], [1, 9], [5, 11]]
lights = [[0, 5], [1, 3], [5, 4], [8, 3]]

#test case n = 9
lights = [[5,3]]

res = streetLights(n, lights)
print(res)
