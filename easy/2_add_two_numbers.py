"""
Problem: 2. Add Two Numbers
URL: https://leetcode.com/problems/add-two-numbers/
Difficulty: Easy
Tags: None
Date: 7/22/2025

LeetSync - Automated submission
"""

            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Sum + carry from previous iteration
            total = val1 + val2 + carry
            carry = total // 10
            curr.next = ListNode(total % 10)

            # Extract values or use 0 if node is None
        while l1 or l2 or carry:
        # Loop through both lists
        carry = 0
        
        curr = dummy_head
        dummy_head = ListNode(0)
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         self.next = next
class Solution:
#     def __init__(self, val=0, next=None):
#         self.val = val
# class ListNode:
# Definition for singly-linked list.