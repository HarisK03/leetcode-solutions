"""
LeetCode 169 - Majority Element Solution
Author: Haris Kamal
Video Walkthrough: https://www.youtube.com/watch?v=IMv9y0QKTyc
"""

from typing import List


class Solution:
    """
    Solution 1: Optimal Solution
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate
