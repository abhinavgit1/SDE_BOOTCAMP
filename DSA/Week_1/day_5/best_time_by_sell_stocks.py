class Solution(object):
    def maxProfit(self, prices):
        min=prices[0]
        maxp=0
        for i in range(1,len(prices)):
            if prices[i]<min:
                min=prices[i]
            pp=prices[i]-min
            if pp>maxp:
                maxp=pp
        return maxp

# LeetCode 121 - Best Time to Buy and Sell Stock
# Pattern: Sliding Window
# Idea: Track the minimum price so far and calculate profit in one pass.
# Time: O(n)
# Space: O(1)