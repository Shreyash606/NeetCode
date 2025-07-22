"""
Problem: 11. Container With Most Water
URL: https://leetcode.com/problems/container-with-most-water/
Difficulty: Easy
Tags: None
Date: 7/22/2025

LeetSync - Automated submission
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l = 0
        r = len(height)-1
        while(l<r):
            h = min(height[l],height[r])
            res = max(res,(h*(r-l)))
            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        return res
        