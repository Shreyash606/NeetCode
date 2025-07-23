"""
Problem: Two Sum
URL: https://leetcode.com/problems/two-sum/
Difficulty: Easy
Language: PY
Tags: None

LeetSync - Auto-generated
Date: 7/22/2025
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        
        for i,num in enumerate(nums):
            complement = target - num
            if complement in hash_map:
                return i,hash_map[complement]
            else:
                hash_map[num] = i