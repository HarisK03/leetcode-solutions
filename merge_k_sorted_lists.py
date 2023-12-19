"""
LeetCode 23 - Merge K Sorted Lists Solution
Author: Haris Kamal
Video Walkthrough: https://www.youtube.com/watch?v=lAMDHQSSQAI
"""

from typing import List, Optional


class ListNode:
    # Definition for singly-linked list.
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Solution 1: Optimal Solution
    Time Complexity: O(nlog(k))
    Space Complexity: O(n)
    """

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(l1, l2):
            dummy = ListNode()
            head = dummy

            while l1 or l2:
                if l1 is None:
                    v1 = float('inf')
                else:
                    v1 = l1.val
                if l2 is None:
                    v2 = float('inf')
                else:
                    v2 = l2.val

                if v1 < v2:
                    l1 = l1.next
                    dummy.next = ListNode(v1)
                else:
                    l2 = l2.next
                    dummy.next = ListNode(v2)

                dummy = dummy.next

            return head.next

        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            sortedLists = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                sortedLists.append(merge(l1, l2))

            lists = sortedLists

        return lists[0]
