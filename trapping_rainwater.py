"""
LeetCode 42 - Trapping Rainwater Solution
Author: Haris Kamal
Video Walkthrough: https://www.youtube.com/watch?v=VfSvo69Oxd4
"""

from typing import List


class Solution:
    """
    Solution 1: Left/Right Arrays Solution
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def trap(self, height: List[int]) -> int:
        left_heights, right_heights = [], []
        for i in range(len(height)):
            left_heights.append(height[i] if len(left_heights) ==
                                0 else max(height[i], left_heights[i-1]))
        for i in range(len(height) - 1, -1, -1):
            right_heights.append(height[i] if len(right_heights) ==
                                 0 else max(height[i], right_heights[-1]))
        right_heights.reverse()
        total = 0
        for i, bar in enumerate(height):
            total += min(left_heights[i], right_heights[i]) - bar
        return total


class Solution:
    """
    Solution 2: Optimal Solution (Two Pointers)
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        left_max, right_max = height[l], height[r]
        total = 0
        while l < r:
            if height[l] <= height[r]:
                l += 1
                left_max = max(left_max, height[l])
                total += left_max - height[l]
            else:
                r -= 1
                right_max = max(right_max, height[r])
                total += right_max - height[r]
        return total
