"""
LeetCode 46 - Permutations Solution
Author: Haris Kamal
Video Walkthrough: https://www.youtube.com/watch?v=d3iYgJ5da0g
"""

from typing import List


class Solution:
    """
    Solution 1: Optimal Solution
    Time Complexity: O(n * n!)
    Space Complexity: O(n * n!)
    """

    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, end):
            if start == end:
                result.append(nums[:])
            for i in range(start, end):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1, end)
                nums[start], nums[i] = nums[i], nums[start]

        result = []
        backtrack(0, len(nums))
        return result
