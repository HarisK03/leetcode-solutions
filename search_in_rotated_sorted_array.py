"""
LeetCode 33 - Search in Rotated Sorted Array Solution
Author: Haris Kamal
Video Walkthrough: https://www.youtube.com/watch?v=RcGo-qjr5UQ
"""

from typing import List


class Solution:
    """
    Solution 1: Binary Search Solution
    Time Complexity: O(log(n))
    Space Complexity: O(1)
    """

    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid

            # left partition
            elif nums[l] <= nums[mid]:
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

            # right partition
            else:
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1
