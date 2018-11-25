#  https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/


class Solution:
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        res = 0
        temp =0
        for i in S:
            if temp == 0 and i==')':
                res = res+1
            elif i == '(':
                temp = temp+1
            else:
                temp =temp-1
        res = res+temp
        return res
