"""
LeetCode 1 - Two Sum Solution
Author: Haris Kamal
Video Walkthrough: https://www.youtube.com/watch?v=9mkQmK_GOx0
"""

from typing import List


class Solution:
    """
    Solution 1: Brute Force Solution
    Time Complexity: O(n²)
    Space Complexity: O(1)
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i] + nums[j] == target):
                    return [i, j]  # or [j, i]


class Solution:
    """
    Solution 2: Optimal Solution (One-pass Hash Table)
    Time Complexity: O(n) average case and O(n²) worst case
    Space Complexity: O(n)
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, num in enumerate(nums):
            if target - num in d:  # complement and O(1) lookup on average
                return [i, d[target - num]]
            d[num] = i
