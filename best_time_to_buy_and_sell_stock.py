"""
LeetCode 121 - Best Time to Buy and Sell Stock Solution
Author: Haris Kamal
Video Walkthrough: https://www.youtube.com/watch?v=Zzg1hMBFKI8
"""

from typing import List


class Solution:
    """
    Solution 1: Optimal Solution
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        max_profit = 0

        while r < len(prices):
            max_profit = max(max_profit, prices[r] - prices[l])

            if prices[r] < prices[l]:
                l = r

            r += 1

        return max_profit
