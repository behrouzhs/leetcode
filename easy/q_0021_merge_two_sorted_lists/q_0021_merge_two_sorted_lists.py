# URL: https://leetcode.com/problems/merge-two-sorted-lists
# Title: 21. Merge Two Sorted Lists
# Difficulty: Easy
# Topics: Linked List, Recursion
# Likes: 22519, Dislikes: 2203
# Submitted: 7.3M, Accepted: 4.8M (65.8%)


question = """
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.
 
Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: list1 = [], list2 = []
Output: []

Example 3:

Input: list1 = [], list2 = [0]
Output: [0]

 
Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def print(self):
        cur = self
        while cur is not None:
            print(cur.val, end=" ")
            cur = cur.next
        print()


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        
        merged = None
        while list1 or list2:
            if merged is None:
                merged = ListNode()
                cur = merged
            else:
                cur.next = ListNode()
                cur = cur.next

            if not list2 or (list1 and list1.val <= list2.val):
                cur.val = list1.val
                list1 = list1.next
            else:
                cur.val = list2.val
                list2 = list2.next
        
        return merged


class Solution2:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        
        cur.next = list1 if list1 else list2
        return dummy.next
