# 42. Trapping Rain Water

**Language:** python  
**Date:** July 22, 2025 at 12:24 PM  
**Problem:** https://leetcode.com/problems/trapping-rain-water/

## Solution

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l,r = 0, len(height) - 1
        leftMax = height[l]
        rightMax = height[r]

        while(l<r):
            if height[l] < height[r]:
                l+=1
```

---
*Automatically synced by LeetSync*
