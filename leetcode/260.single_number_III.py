# Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. 
# Find the two elements that appear only once. You can return the answer in any order.

# You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.


class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        xor = 0
        for num in nums:
            xor ^= num

        mask = 1
        while xor & mask == 0:
            mask <<= 1

        num1, num2 = 0, 0
        for num in nums:
            if num & mask == 0:
                num1 ^= num
            else:
                num2 ^= num

        return [num1, num2]