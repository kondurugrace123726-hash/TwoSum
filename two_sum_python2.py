"""
Problem: Two Sum

Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

Approach:
- Use a hashmap to store number → index.
- For each number, check if target - number already exists.

Time Complexity: O(n)
Space Complexity: O(n)
"""
from typing import List

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index_map = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in index_map:
                return [index_map[complement], i]
            index_map[nums[i]] = i
        return []

