class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def exact(k):
            left=0
            freq={}
            c=0
            for i in range(len(nums)):
                if nums[i] in freq:
                    freq[nums[i]]+=1
                else:
                    freq[nums[i]]=1
                while len(freq)>k:
                    freq[nums[left]]-=1
                    if freq[nums[left]]==0:
                        del freq[nums[left]]
                    left=left+1
                c=c+(i-left+1)
            return c
        return exact(k)-exact(k-1)