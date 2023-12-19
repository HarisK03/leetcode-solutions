"""
LeetCode 128 - Longest Consecutive Sequence Solution
Author: Haris Kamal
Video Walkthrough: https://www.youtube.com/watch?v=gkjxWzaMURQ
"""

from typing import List


class Solution:
    """
    Solution 1: Optimal Solution
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        res = 0

        for num in nums:
            if num - 1 not in nums_set:
                length = 0
                while num + length in nums_set:
                    length += 1
                res = max(res, length)

        return res
