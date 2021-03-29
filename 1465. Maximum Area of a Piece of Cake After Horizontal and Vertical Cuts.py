'''
1465. Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts

Input: h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3]
Output: 4 
Explanation: The figure above represents the given rectangular cake.
Red lines are the horizontal and vertical cuts. After you cut the cake, the green piece of cake has the maximum area.

Refer this link to view the question
https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/

'''

def maxArea(h, w, horizontalCuts, verticalCuts):
        hcuts = sorted(horizontalCuts)
        vcuts = sorted(verticalCuts)
        
        if(hcuts[-1] < h):
            hcuts.append(h)
        if(vcuts[-1] < w):
            vcuts.append(w)
        
        h_max_intervals = 0
        for i in range(len(hcuts)):
            interval = hcuts[i]
            if(i > 0):
                interval -= hcuts[i-1]
            
            if(interval > h_max_intervals):
                h_max_intervals = interval
                
        v_max_intervals = 0
        for i in range(len(vcuts)):
            interval = vcuts[i]
            if(i > 0):
                interval -= vcuts[i-1]
            
            if(interval > v_max_intervals):
                v_max_intervals = interval
        return (h_max_intervals*v_max_intervals) % (10**9 + 7)

h = 5
w = 4
horizontalCuts = [3]
verticalCuts = [3]

res = maxArea(h, w, horizontalCuts, verticalCuts)
print(res)
