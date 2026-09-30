class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequency = {}
        max_freq = 0
        left = 0
        result = 0

        for right in range(len(s)):
            frequency[s[right]] = 1 + frequency.get(s[right], 0)
            max_freq = max(max_freq, frequency[s[right]])

            while (right - left + 1) - max_freq > k:
                frequency[s[left]] -= 1
                left += 1
            
            result = max(result, right - left + 1)
        
        return result