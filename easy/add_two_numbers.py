"""
Problem: Add Two Numbers
URL: https://leetcode.com/problems/add-two-numbers/
Difficulty: Easy
Language: PY
Tags: None

LeetSync - Auto-generated
Date: 7/22/2025
"""

# Loop through both lists
        while l1 or l2 or carry:
            # Extract values or use 0 if node is None
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Sum + carry from previous iteration
            total = val1 + val2 + carry
            carry = total // 10
            curr.next = ListNode(total % 10)

            # Move pointers forward
            curr = curr.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy_head.next