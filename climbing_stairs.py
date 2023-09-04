"""
LeetCode 70 - Climbing Stairs Solution
Author: Haris Kamal
Video Walkthrough: https://www.youtube.com/watch?v=SghqtkIuZe4
"""


class Solution:
    """
    Solution 1: Recursion with Memoization
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def climbStairs(self, n: int) -> int:
        memo = {}

        def climb(n):
            if n in memo:
                return memo[n]

            if n <= 2:
                return n

            memo[n] = climb(n - 1) + climb(n - 2)
            return memo[n]

        return climb(n)


class Solution:
    """
    Solution 2: Dynamic Programming
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        prev1, prev2 = 1, 2

        for _ in range(3, n + 1):
            prev1, prev2 = prev2, prev1 + prev2

        return prev2


class Solution:
    """
    Solution 3: Fiboncci Sequence
    Time Complexity: O(1)
    Space Complexity: O(1)
    """

    def climbStairs(self, n: int) -> int:
        n += 1
        a = (1 + 5 ** 0.5) / 2
        b = (1 - 5 ** 0.5) / 2
        return int((a ** n - b ** n) / (5 ** 0.5))
