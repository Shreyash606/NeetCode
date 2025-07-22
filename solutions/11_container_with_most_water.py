# 11. Container With Most Water

**Language:** python  
**Date:** July 22, 2025 at 12:23 PM  
**Problem:** https://leetcode.com/problems/container-with-most-water/submissions/1707549706/

## Solution

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l = 0
        r = len(height)-1
        while(l<r):
            h = min(height[l],height[r])
            res = max(res,(h*(r-l)))
            if height[l] < height[r]:
                l+=1
```

---
*Automatically synced by LeetSync*
