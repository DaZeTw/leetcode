class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = 0 
        end = 1
        ans = 0
        while end < len(prices):
            profit = prices[end]-prices[start]
            ans = max(ans,profit)
            if (prices[end]<prices[start]): start = end
            end +=1
        return ans