class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        c=0
        s=0
        freq={0:1}
        for i in range(len(nums)):
            s=s+nums[i]
            r=s%k
            if r in freq:
                c=c+freq[r]
                freq[r]+=1
            else:
                freq[r]=1
        return c
        