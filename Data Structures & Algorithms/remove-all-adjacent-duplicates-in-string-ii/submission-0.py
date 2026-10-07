class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # deeedbbcccbdaa
        # k = 3

        # first removal
        # eee
        # ddbbcccbdaa

        # second removal
        # ccc
        # ddbbbdaa

        # third removal
        # bbb
        # dddaa

        # fourth removal
        # ddd
        # aa

        stack = []  # ([char, count])
        n = len(s)

        for c in s:
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1
            else:
                stack.append([c, 1])
            if stack[-1][1] == k:
                stack.pop()

        result = ""

        for char, count in stack:
            result += char * count

        return result
        # s = list(s)
        # i = 0

        # while i < n:
        #     if i == 0 or s[i] != s[i-1]:
        #         stack.append(1)
        #     else:
        #         stack[-1] += 1
        #         if stack[-1] == k:
        #             stack.pop()
        #             del s[i-k+1: i+1]
        #             i -= k
        #             n -= k
        #     i += 1
        
        # return ''.join(s)
            
        