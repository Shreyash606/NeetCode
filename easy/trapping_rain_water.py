"""
Problem: Trapping Rain Water
URL: https://leetcode.com/problems/trapping-rain-water/submissions/1707844095/
Difficulty: Easy
Tags: None
Date: 7/22/2025

LeetSync - Automated submission
"""

class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l,r = 0, len(height) - 1
        leftMax = height[l]
        rightMax = height[r]

        while(l<r):
            if height[l] < height[r]:
                l+=1
                leftMax = max(leftMax,height[l])
                res += leftMax - height[l]
            else:
                r-=1
                rightMax = max(rightMax,height[r])
                res += rightMax - height[r]
        return res

        # while(l<r):
        #     if height[l] < height[r]:
        #         l+=1
        #         leftMax = max(leftMax,height[l])
        #         res += leftMax - height[l]
        #     else:
        #         r-=1
        #         rightMax = max(rightMax, height[r])
        #         res += rightMax - height[r]
        # return res
        