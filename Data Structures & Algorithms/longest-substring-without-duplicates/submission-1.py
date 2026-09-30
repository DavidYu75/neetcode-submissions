class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = {}
        left = 0
        result = 0

        for right in range(len(s)):
            if s[right] in window:
                left = max(left, window[s[right]] + 1)
            window[s[right]] = right
            result = max(result, right - left + 1)

        return result