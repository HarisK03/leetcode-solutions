"""
LeetCode 22 - Generate Parentheses Solution
Author: Haris Kamal
Video Walkthrough: https://www.youtube.com/watch?v=0jAdaKQJ8Eg
"""

from typing import List


class Solution:
    """
    Solution 1: Optimal (Backtracking) Solution
    Time Complexity: O(4^n/sqrt(n))
    Space Complexity: O(4^n/sqrt(n))
    """

    def generateParenthesis(self, n: int) -> List[str]:
        def generate(open, close, s):
            if len(s) == n * 2:
                res.append(s)
                return

            if open < n:
                generate(open + 1, close, s + '(')

            if open > close:
                generate(open, close + 1, s + ')')

        res = []
        generate(0, 0, "")
        return res
