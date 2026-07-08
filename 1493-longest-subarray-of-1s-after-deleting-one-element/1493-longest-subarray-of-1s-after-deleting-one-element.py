class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans=0
        left=0
        z=0
        for right in range(len(nums)):
            if nums[right]==0:
                z=z+1
            while z>1:
                if nums[left]==0:
                    z=z-1
                left=left+1
            ans=max(ans,right-left)
        return ans