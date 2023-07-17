"""
LeetCode 20 - Valid Parentheses
Author: Haris Kamal
Video Walkthrough: https://www.youtube.com/watch?v=a5N9WXNrT1k
"""


class Solution:
    """
    Solution 1: Optimal Solution
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def isValid(self, s: str) -> bool:
        stack = []

        for p in s:
            if p in ["(", "{", "["]:
                stack.append(p)
            elif len(stack) == 0:
                return False
            else:
                last = stack.pop()
                if last == "(" and p != ")" or last == "{" and p != "}" or last == "[" and p != "]":
                    return False

        return len(stack) == 0
