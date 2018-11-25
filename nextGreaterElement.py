# https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res=[]
        for i in nums1: 
            s = nums2[:]
            temp = -1
            #print(s)
            q = s.pop()
            while q != i:
                if q>i:
                    temp =q
                q=s.pop()
            res.append(temp)
        return res


