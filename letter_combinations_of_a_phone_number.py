"""
LeetCode 17 - Letter Combinations of a Phone Number Solution
Author: Haris Kamal
Video Walkthrough: https://www.youtube.com/watch?v=hUNjuTXRSTM
"""

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        dToC = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(i, path):
            if i == len(digits):
                res.append(path)
                return

            for c in dToC[digits[i]]:
                backtrack(i + 1, path + c)

        if digits:
            backtrack(0, "")

        return res
