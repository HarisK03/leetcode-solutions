"""
LeetCode 55 - Jump Game Solution
Author: Haris Kamal
Video Walkthrough: https://www.youtube.com/watch?v=bZJqh1LuIJk
"""

from typing import List


class Solution:
    """
    Solution 1: Optimal Solution
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return goal == 0
