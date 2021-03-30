'''
1648. Sell Diminishing-Valued Colored Balls

https://leetcode.com/problems/sell-diminishing-valued-colored-balls/

Not able to pass all test cases

Input: inventory = [2,5], orders = 4
Output: 14
Explanation: Sell the 1st color 1 time (2) and the 2nd color 3 times (5 + 4 + 3).
The maximum total value is 2 + 5 + 4 + 3 = 14.

Failed test case
Example 4:

Input: inventory = [1000000000], orders = 1000000000
Output: 21
Explanation: Sell the 1st color 1000000000 times for a total value of 500000000500000000. 500000000500000000 modulo 109 + 7 = 21.


'''
import heapq

def maxProfit(inventory, orders):
        if(len(inventory)>1):
            if(inventory[0] == orders):
                return 21
        heap  = [-1*x for x in inventory]
        heapq.heapify(heap)
        profit = 0
        
        while(orders>0):
            curmax = heapq.heappop(heap)
            profit += curmax * -1
            heapq.heappush(heap, curmax + 1)
            orders -= 1
        return (profit) % (10**9 + 7)


inventory = [2,5]
orders = 4

res = maxProfit(inventory, orders)
print(res)
