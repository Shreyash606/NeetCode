"""
Problem: Add Two Numbers
URL: https://leetcode.com/problems/add-two-numbers/
Difficulty: Easy
Language: PY
Tags: None

LeetSync - Auto-generated
Date: 7/22/2025
"""

# Definition for singly-linked list.# Definition for singly-linked list.
# class ListNode:# class ListNode:
#     def __init__(self, val=0, next=None):#     def __init__(self, val=0, next=None):
#         self.val = val#         self.val = val
#         self.next = next#         self.next = next
class Solution:class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0)        dummy_head = ListNode(0)
        curr = dummy_head        curr = dummy_head
        carry = 0        carry = 0
                
        # Loop through both lists        # Loop through both lists
        while l1 or l2 or carry:        while l1 or l2 or carry:
            # Extract values or use 0 if node is None            # Extract values or use 0 if node is None
            val1 = l1.val if l1 else 0            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0            val2 = l2.val if l2 else 0

            # Sum + carry from previous iteration            # Sum + carry from previous iteration
            total = val1 + val2 + carry            total = val1 + val2 + carry
            carry = total // 10            carry = total // 10
            curr.next = ListNode(total % 10)            curr.next = ListNode(total % 10)