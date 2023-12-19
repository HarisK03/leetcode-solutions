"""
LeetCode 238 - Product of Array Except Self Solution
Author: Haris Kamal
Video Walkthrough: https://www.youtube.com/watch?v=RUxgZn5mlr8
"""

from typing import List


class Solution:
    """
    Solution 1: Optimal Solution
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)
        prefix, postfix = 1, 1

        for i in range(len(nums)):
            answer[i] *= prefix
            prefix *= nums[i]

            answer[-1 - i] *= postfix
            postfix *= nums[-1 - i]

        return answer
