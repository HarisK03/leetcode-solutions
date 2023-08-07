"""
LeetCode 56 - Merge Intervals Solution
Author: Haris Kamal
Video Walkthrough: https://www.youtube.com/watch?v=t89eLCbdaos
"""

from typing import List


class Solution:
    """
    Solution 1: Optimal Solution
    Time Complexity: O(nlog(n))
    Space Complexity: O(n)
    """

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        merged_intervals = [intervals[0]]

        for interval in intervals[1:]:
            if interval[0] <= merged_intervals[-1][1]:
                merged_intervals[-1][1] = max(merged_intervals[-1]
                                              [1], interval[1])
            else:
                merged_intervals.append(interval)

        return merged_intervals
