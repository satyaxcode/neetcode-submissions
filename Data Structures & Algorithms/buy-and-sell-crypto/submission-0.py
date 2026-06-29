class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lb, rs = 0, 1
        maxP = 0

        while rs < len(prices):
            if prices[lb] < prices[rs]:
                profit = prices[rs] - prices[lb]
                maxP = max(maxP, profit)
            else:
                lb = rs
            rs += 1
        return maxP