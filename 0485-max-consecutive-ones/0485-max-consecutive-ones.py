class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left=0
        mx=0
        for right in range(len(nums)):
            if nums[right]!=0:
                curr=right-left+1
                mx=max(mx,curr)
            else:
                curr=0
                left=right+1
        return mx
