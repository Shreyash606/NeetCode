"""
Problem: Two Sum
URL: https://leetcode.com/problems/two-sum/description/
Difficulty: Easy
Tags: None
Date: 7/22/2025

LeetSync - Automated submission
"""

class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l,r = 0, len(height) - 1
        leftMax = height[l]
        rightMax = height[r]

        while(l<r):
            if height[l] < height[r]:
                l+=1
                leftMax = max(leftMax,height[l])
                res += leftMax - height[l]
            else:
                r-=1
                rightMax = max(rightMax,height[r])
                res += rightMax - height[r]
        return res