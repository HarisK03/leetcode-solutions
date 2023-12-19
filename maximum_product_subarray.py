"""
LeetCode 152 - Maximum Product Subarray Solution
Author: Haris Kamal
Video Walkthrough: https://www.youtube.com/watch?v=KUcBD1jZxco
"""

from typing import List


class Solution:
    """
    Solution 1: Optimal Solution
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def maxProduct(self, nums: List[int]) -> int:
        max_product = nums[0]
        min_product = nums[0]
        res = max_product

        for i in range(1, len(nums)):
            if nums[i] < 0:
                max_product, min_product = min_product, max_product

            max_product = max(nums[i], max_product * nums[i])
            min_product = min(nums[i], min_product * nums[i])

            res = max(res, max_product)

        return res
