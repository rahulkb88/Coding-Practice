# https://leetcode.com/problems/count-binary-substrings/submissions/

class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        g = []
        temp = 1
        cur = s[0]
        for i in range(1,len(s)):
            if cur == s[i]:
                temp = temp+1
            else:
                g.append(temp)
                temp = 1
                cur = s[i]
        g.append(temp)
        print(g)
        for i in range(len(g)-1):
            res = res+min(g[i], g[i+1])
        return res
