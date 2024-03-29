"""
LeetCode 4 - Median of Two Sorted Arrays Solution
Author: Haris Kamal
Video Walkthrough: https://www.youtube.com/watch?v=z44F7FbMIQw
"""

from typing import List


class Solution:
    """
    Solution 1: Binary Search Solution
    Time Complexity: O(log(min(m, n)))
    Space Complexity: O(1)
    """

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        start, end = 0, len(nums1)
        x, y = len(nums1), len(nums2)

        while start <= end:
            partition_x = (start + end) // 2
            partition_y = (x + y + 1) // 2 - partition_x

            max_left_x = float(
                '-inf') if partition_x == 0 else nums1[partition_x - 1]
            min_right_x = float(
                'inf') if partition_x == x else nums1[partition_x]

            max_left_y = float(
                '-inf') if partition_y == 0 else nums2[partition_y - 1]
            min_right_y = float(
                'inf') if partition_y == y else nums2[partition_y]

            if max_left_x <= min_right_y and max_left_y <= min_right_x:
                if (x + y) % 2 == 0:
                    return (max(max_left_x, max_left_y) + min(min_right_x, min_right_y)) / 2
                else:
                    return max(max_left_x, max_left_y)
            elif max_left_x > min_right_y:
                end = partition_x - 1
            else:
                start = partition_x + 1
