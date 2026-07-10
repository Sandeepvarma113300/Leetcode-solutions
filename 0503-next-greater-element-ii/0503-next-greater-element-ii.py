class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack=[]
        p=nums+nums
        res=[-1]*len(nums)
        for i in range(len(p)-1,-1,-1):
            while stack and stack[-1]<=p[i]:
                stack.pop()
            if i<len(nums) and stack:
                res[i]=stack[-1]
            stack.append(p[i])
        return res
