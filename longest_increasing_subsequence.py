"""
LeetCode 300 - Longest Increasing Subsequence Solution
Author: Haris Kamal
Video Walkthrough: https://www.youtube.com/watch?v=AQ8mHCeEK_s
"""

from typing import List


class Solution:
    """
    Solution 1: Optimal Solution
    Time Complexity: O(nlog(n))
    Space Complexity: O(n)
    """

    def lengthOfLIS(self, nums: List[int]) -> int:
        res = [nums[0]]

        for num in nums[1:]:
            if num > res[-1]:
                res.append(num)
            else:
                l, r = 0, len(res) - 1
                while l < r:
                    mid = l + (r - l) // 2
                    if res[mid] < num:
                        l = mid + 1
                    else:
                        r = mid
                res[l] = num

        return len(res)
