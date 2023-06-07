"""
LeetCode 2 - Add Two Numbers Solution
Author: Haris Kamal
Video Walkthrough: https://www.youtube.com/watch?v=s2_8re0tG_8
"""

from typing import Optional


class ListNode:
    # Definition for singly-linked list.
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Solution 1: Optimal Solution
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head, carry = l1, False

        while l1 or l2:
            # adjust l1 if len(l1) < len(l2)
            if not l1.next and l2:
                l1.next, l2.next = l2.next, l1.next

            # replace None with 0
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            carry, l1.val = divmod(v1 + v2 + carry, 10)

            prev = l1
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry:
            prev.next = ListNode(carry)

        return head  # returns mutated input
