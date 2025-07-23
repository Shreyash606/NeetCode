"""
Problem: Add Two Numbers
URL: https://leetcode.com/problems/add-two-numbers/
Difficulty: Easy
Language: PY
Tags: None

LeetSync - Auto-generated
Date: 7/22/2025
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        curr = dummy_head
        carry = 0
        
        # Loop through both lists
        while l1 or l2 or carry:
            # Extract values or use 0 if node is None
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Sum + carry from previous iteration
            total = val1 + val2 + carry
            carry = total // 10
            curr.next = ListNode(total % 10)