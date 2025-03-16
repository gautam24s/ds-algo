# Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

# Return any possible rearrangement of s or return "" if not possible.

 

# Example 1:

# Input: s = "aab"
# Output: "aba"
# Example 2:

# Input: s = "aaab"
# Output: ""
 

# Constraints:

# 1 <= s.length <= 500
# s consists of lowercase English letters.


import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        if n == 1:
            return s
        
        # Count the frequency of each character
        char_count = Counter(s)

        # Create a max heap based on the frequency of characters
        max_heap = [(-count, char) for char, count in char_count.items()]
        heapq.heapify(max_heap)
        
        prev_count, prev_char = 0, ''
        result = []
        
        while max_heap:
            count, char = heapq.heappop(max_heap)
            result.append(char)
            
            # If there was a previous character, push it back into the heap
            if prev_count < 0:
                heapq.heappush(max_heap, (prev_count, prev_char))
            
            # Update previous character and count
            prev_count, prev_char = count + 1, char
        
        result_str = ''.join(result)
        
        # Check if the reorganized string is valid
        for i in range(1, len(result_str)):
            if result_str[i] == result_str[i - 1]:
                return ""
        
        return result_str

# Example usage
print(Solution().reorganizeString("aaab"))  # Output: "aba"