"""
LeetCode 206 - Reverse Linked List Solution
Author: Haris Kamal
Video Walkthrough: https://www.youtube.com/watch?v=war0ysA1KDg
"""

from typing import Optional


class ListNode:
    # Definition for singly-linked list.
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Solution 1: Iterative Solution
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev


class Solution:
    """
    Solution 2: Recursive Solution
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        new_head = self.reverseList(head.next)

        head.next.next = head
        head.next = None

        return new_head
