"""
LeetCode 53 - Maximum Subarray Solution
Author: Haris Kamal
Video Walkthrough: https://www.youtube.com/watch?v=tCtOojn-k08
"""

from typing import List


class Solution:
    """
    Solution 1: Brute Force Solution (Time Limit Exceeded on LeetCode)
    Time Complexity: O(n²)
    Space Complexity: O(1)
    """

    def maxSubArray(self, nums: List[int]) -> int:
        largest = nums[0]
        for i in range(len(nums)):
            curr_sum = 0
            for j in range(i, len(nums)):
                curr_sum += nums[j]
                largest = max(largest, curr_sum)
        return largest


class Solution:
    """
    Solution 2: Optimal Solution
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def maxSubArray(self, nums: List[int]) -> int:
        largest = nums[0]
        curr_sum = 0
        for num in nums:
            if curr_sum < 0:  # negative prefix
                curr_sum = 0
            curr_sum += num
            largest = max(largest, curr_sum)
        return largest
