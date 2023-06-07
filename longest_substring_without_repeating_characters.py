"""
LeetCode 3 - Longest Substring Without Repeating Characters Solution
Author: Haris Kamal
Video Walkthrough: https://www.youtube.com/watch?v=VP4gPDmfGyM
"""


class Solution:
    """
    Solution 1: Brute Force Solution
    Time Complexity: O(n²) average case and O(n³) worst case
    Space Complexity: O(n)
    """

    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        for i in range(len(s)):
            char_set = set()  # unique characters
            for char in range(i, len(s)):
                if s[char] in char_set:  # character has been seen already
                    break
                char_set.add(s[char])
                length = max(length, len(char_set))
        return length


class Solution:
    """
    Solution 2: Optimal Solution (One-pass Sliding Window)
    Time Complexity: O(n) average and O(n²) worst case
    Space Complexity: O(n)
    """

    def lengthOfLongestSubstring(self, s: str) -> int:
        start, length = 0, 0
        char_map = {}
        for end, char in enumerate(s):
            if char in char_map and char_map[char] >= start:  # update start
                length = max(length, end - start)
                start = char_map[char] + 1
            char_map[char] = end  # update end
        return max(length, len(s) - start)
