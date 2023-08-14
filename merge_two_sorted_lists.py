"""
LeetCode 21 - Merge Two Sorted Lists Solution
Author: Haris Kamal
Video Walkthrough: https://www.youtube.com/watch?v=7cC1KKRCC4M
"""

from typing import Optional


class ListNode:
    # Definition for singly-linked list.
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Solution 1: Optimal Solution (Recursive)
    Time Complexity: O(n + m)
    Space Complexity: O(1)
    """

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1

        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
