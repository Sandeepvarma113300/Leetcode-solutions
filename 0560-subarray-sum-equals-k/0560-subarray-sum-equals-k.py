class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        s=0
        c=0
        freq={0:1}
        for i in range(len(nums)):
            s=s+nums[i]
            if s-k in freq:
                c=c+freq[s-k]
            if s in freq:
                freq[s]+=1
            else:
                freq[s]=1
        print(freq)
        return c
