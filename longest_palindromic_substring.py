"""
LeetCode 5 - Longest Palindromic Substring Solution
Author: Haris Kamal
Video Walkthrough: https://www.youtube.com/watch?v=yIOcadnp6TM
"""


class Solution:
    """
    Solution 1: Expand From Center Solution
    Time Complexity: O(n²)
    Space Complexity: O(1)

    Note: A more optimal (linear time) solution is possible using Manacher's algorithm
    """

    def longestPalindrome(self, s: str) -> str:
        longest_start, longest_end = 0, 1

        for index in range(len(s)):
            for left, right in (index, index), (index, index + 1):
                while 0 <= left and right < len(s) and s[left] == s[right]:
                    left -= 1
                    right += 1
                if (right - left) - 1 > longest_end - longest_start:
                    longest_start, longest_end = left + 1, right

        return s[longest_start:longest_end]
