# Given an integer array `nums` of unique elements, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.


# Approach 1: Backtracking
# Time complexity: O(N * 2^N)
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        subsets = []
        def backtrack(start, path):
            subsets.append(path)
            for i in range(start, len(nums)):
                backtrack(i + 1, path + [nums[i]])
        backtrack(0, [])
        return subsets
