"""
LeetCode 39 - Combination Sum Solution
Author: Haris Kamal
Video Walkthrough: https://www.youtube.com/watch?v=5iFzlvz67QA
"""

from typing import List


class Solution:
    """
    Solution 1: Optimal Solution
    Time Complexity: O(k*2^n)
    Space Complexity: O(n)
    """

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            elif i >= len(candidates) or total > target:
                return

            curr.append(candidates[i])
            dfs(i, curr, total + candidates[i])
            curr.pop()
            dfs(i + 1, curr, total)

        dfs(0, [], 0)
        return res
