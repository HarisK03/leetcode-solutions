"""
LeetCode 198 - House Robber Solution
Author: Haris Kamal
Video Walkthrough: https://www.youtube.com/watch?v=ZjdmqCnJJLg
"""

from typing import List


class Solution:
    """
    Solution 1: Optimal Solution
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def rob(self, nums: List[int]) -> int:
        prev1, prev2 = 0, 0

        for num in nums:
            rob = max(prev1 + num, prev2)
            prev1 = prev2
            prev2 = rob

        return prev2
