class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_characters, t_characters = {}, {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            s_characters[s[i]] = 1 + s_characters.get(s[i], 0)
            t_characters[t[i]] = 1 + t_characters.get(t[i], 0)
        
        return s_characters == t_characters