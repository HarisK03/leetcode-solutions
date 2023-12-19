"""
LeetCode 49 - Group Anagrams Solution
Author: Haris Kamal
Video Walkthrough: https://www.youtube.com/watch?v=5AaXIgXCBt8
"""

from collections import defaultdict
from typing import List


class Solution:
    """
    Solution 1: Optimal Solution
    Time Complexity: O(nlog(k))
    Space Complexity: O(n)
    """

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            freq = [0] * 26
            for char in s:
                freq[ord(char) - ord("a")] += 1
            res[tuple(freq)].append(s)

        return res.values()
