class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        left = 0 #left pointer
        right = 1 #right pointer

        max_profit = 0
        print(len(prices))
        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right]-prices[left]
                max_profit = max(max_profit, profit)
            else:
                left = right
            right += 1
        return max_profit
        