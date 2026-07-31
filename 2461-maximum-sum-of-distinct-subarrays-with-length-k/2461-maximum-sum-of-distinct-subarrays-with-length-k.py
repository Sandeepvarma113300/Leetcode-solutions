class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        w=nums[:k]
        mx = 0
        s=0 
        freq={}
        for i in w:
            s=s+i
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        if len(freq)==k:
            mx=s
        for i in range(k,len(nums)):
            left=nums[i-k]
            right=nums[i]
            s-=left
            freq[left]-=1
            if freq[left]==0:
                del freq[left]
            s+=right
            if right in freq:
                freq[right]+=1
            else:
                freq[right]=1
            if len(freq)==k:
                mx=max(s,mx)
        return mx


