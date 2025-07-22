# Add Two Numbers

**Language:** python  
**Date:** July 22, 2025 at 10:57 AM  
**Problem:** https://leetcode.com/problems/add-two-numbers/submissions/1707377928/

## Solution

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        curr = dummy_head
        carry = 0
```

---
*Automatically synced by LeetSync*
