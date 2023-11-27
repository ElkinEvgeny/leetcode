class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sum=0
        num = prices[0]
        for i in prices:
            if i < num:
                num=i
            sum = max(sum, i-num)
        return sum