#https://leetcode.com/problems/degree-of-an-array/

class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lnum = len(nums)
        if lnum == 0 or lnum == 1:
            return lnum
        res = lnum
        dic={}
        for i in nums:
            if i in dic:
                dic[i] = dic[i]+1
            else:
                dic[i] = 1

        degree=0
        nodes=[]
        for i in dic:
            if dic[i]>degree:
                degree = dic[i]
                nodes=[i]
            elif dic[i]==degree:
                nodes.append(i)
        #print(dic)
        #print(nodes)

        first = {}
        last = {}
        for i in range(lnum):
            if nums[i] in nodes:
                if nums[i]  not in first:
                    first[nums[i]] = i
                else:
                    last[nums[i]] = i
        #print(first, last)
        if len(last) == 0:
            return 1

        for i in last:
            if last[i] - first[i] + 1 < res:
                res = last[i] - first[i] + 1

        return res
