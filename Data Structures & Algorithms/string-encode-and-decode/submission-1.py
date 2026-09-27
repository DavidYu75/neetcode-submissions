class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for s in strs:
            result += str(len(s)) + '#' + s
        
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != '#':
                j += 1
            
            word_length = int(s[i:j])
            result.append(s[j+1 : word_length + j + 1])

            i = j + 1 + word_length
        
        return result

