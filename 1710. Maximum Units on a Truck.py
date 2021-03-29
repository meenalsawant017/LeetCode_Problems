'''
1710. Maximum Units on a Truck

Example 1:

Input: boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4
Output: 8
Explanation: There are:
- 1 box of the first type that contains 3 units.
- 2 boxes of the second type that contain 2 units each.
- 3 boxes of the third type that contain 1 unit each.
You can take all the boxes of the first and second types, and one box of the third type.
The total number of units will be = (1 * 3) + (2 * 2) + (1 * 1) = 8.
Example 2:

Input: boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10
Output: 91
'''

def maximumUnits(boxTypes, truckSize):

        boxTypes.sort(key = lambda x:x[1], reverse = True)
        maxUnit = 0
        
        for i in range(len(boxTypes)):
            if(truckSize <= boxTypes[i][0]):
                return maxUnit + truckSize * boxTypes[i][1]
            else:
                maxUnit += boxTypes[i][0] *boxTypes[i][1]
                truckSize -= boxTypes[i][0]
        return maxUnit

boxTypes = [[1,3],[2,2],[3,1]]
truckSize = 4

#test case 2
boxTypes = [[5,10],[2,5],[4,7],[3,9]]
truckSize = 10

res = maximumUnits(boxTypes, truckSize)
print(res)
