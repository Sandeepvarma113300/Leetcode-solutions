class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        res=[-1]*len(nums2)
        for i in range(len(nums2)-1,-1,-1):
            while stack and stack[-1]<=nums2[i]:
                stack.pop()
            if stack:
                res[i]=stack[-1]
            stack.append(nums2[i])
        freq={}
        for i in range(len(nums2)):
            freq[nums2[i]]=res[i]
        ans=[]
        for i in nums1:
            ans.append(freq[i])
        return ans