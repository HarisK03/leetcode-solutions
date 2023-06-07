"""
LeetCode 15 - 3Sum Solution
Author: Haris Kamal
Video Walkthrough: https://www.youtube.com/watch?v=JBUDTXXaBh0
"""

from typing import List


class Solution:
    """
    Solution 1: Optimal Solution
    Time Complexity: O(n²)
    Space Complexity: O(1) / O(n) depending on consideration of result array
    """

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # O(nlogn) time complexity and O(n) space complexity (Timsort)
        result = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue  # skip duplicates

            l, r = i + 1, len(nums) - 1

            while l < r:
                triplet = nums[i] + nums[l] + nums[r]
                if triplet < 0:
                    l += 1
                elif triplet > 0:
                    r -= 1
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1  # skip duplicates
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1  # skip duplicates
                    l += 1
                    r -= 1

        return result
