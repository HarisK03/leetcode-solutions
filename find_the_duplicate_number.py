"""
LeetCode 287 - Find the Duplicate Number Solution
Author: Haris Kamal
Video Walkthrough: https://www.youtube.com/watch?v=UFAEGRkpV8s
"""

from typing import List


class Solution:
    """
    Solution 1: Slow and Fast Pointers Solution
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        slow = nums[0]

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
