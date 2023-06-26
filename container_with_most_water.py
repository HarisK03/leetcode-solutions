"""
LeetCode 11 - Container With Most Water
Author: Haris Kamal
Video Walkthrough: https://www.youtube.com/watch?v=-CRqYDrEsJw
"""

from typing import List


class Solution:
    """
    Solution 1: Two Pointers
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0
        while l < r:
            res = max(res, (r - l) * min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res
