# Given two integers left and right that represent the range [left, right], 
# return the bitwise AND of all numbers in this range, inclusive.


class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        
        shift = 0
        while left < right:
            left >>= 1
            right >>= 1
            shift += 1
        return left << shift
    

print(Solution().rangeBitwiseAnd(5, 7))  # Output: 4