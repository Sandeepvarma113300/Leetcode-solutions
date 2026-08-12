class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        left=0
        freq={}
        ans=0
        for right in range(len(nums)):
            if nums[right] in freq:
                freq[nums[right]]+=1
            else:
                freq[nums[right]]=1
            while freq[nums[right]]>k:
                freq[nums[left]]-=1
                if freq[nums[left]]==0:
                    del freq[nums[left]]
                left=left+1
            curr=right-left+1
            ans=max(ans,curr)
        return ans
        