"""
LeetCode 287 - Find the Duplicate Number Solution
Author: Haris Kamal
Video Walkthrough: https://www.youtube.com/watch?v=UFAEGRkpV8s
"""


class Solution:
    """
    Solution 1: Slow and Fast Pointers
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def findDuplicate(self, nums):
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
