"""
LeetCode 560 - Subarray Sum Equals K Solution
Author: Haris Kamal
Video Walkthrough: https://www.youtube.com/watch?v=Rokwl5xfVPw
"""

from typing import List


class Solution:
    """
    Solution 1: Prefix Sum Solution
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_map = {0: 1}
        total_sum = 0
        res = 0

        for num in nums:
            total_sum += num

            if total_sum - k in prefix_map:
                res += prefix_map[total_sum - k]

            if total_sum in prefix_map:
                prefix_map[total_sum] += 1
            else:
                prefix_map[total_sum] = 1

        return res
