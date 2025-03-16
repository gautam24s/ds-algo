# Write a function to find the longest common prefix string
# amongst an array of strings.

# If there is no common prefix, return an empty string "".


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""

        min_length = min(len(s) for s in strs)

        common_prefix = ""

        for i in range(min_length):
            current_char = strs[0][i]

            if all(s[i] == current_char for s in strs):
                common_prefix += current_char
            else:
                break

        return common_prefix
