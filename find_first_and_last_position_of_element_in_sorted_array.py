"""
LeetCode 49 - Find First and Last Position of Element in Sorted Array Solution
Author: Haris Kamal
Video Walkthrough: https://www.youtube.com/watch?v=jtLadaPugFE
"""

from typing import List


class Solution:
    """
    Solution 1: Optimal Solution
    Time Complexity: O(nlog(n))
    Space Complexity: O(1)
    """

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(target):
            l, r = 0, len(nums)

            while l < r:
                mid = (l + r) // 2
                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid

            return l

        left = binary_search(target)
        right = binary_search(target + 1) - 1

        if left <= right:
            return [left, right]

        return [-1, -1]
