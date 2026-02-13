from typing import List

"""
Problem: Two Sum

Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_ind = {}
        for i, num in enumerate(nums):
            if target - num in val_ind:
                return [val_ind[target - num], i]
            val_ind[num] = i


if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum([2, 7, 11, 15], 9))  # Expected output: [0, 1]