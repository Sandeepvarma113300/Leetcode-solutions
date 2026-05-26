class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        p=0
        freq={0:1}
        c=0
        for i in nums:
            p=p+i
            if p-k in freq:
                c=c+freq[p-k]
            if p in freq:
                freq[p]+=1
            else:
                freq[p]=1
        return c