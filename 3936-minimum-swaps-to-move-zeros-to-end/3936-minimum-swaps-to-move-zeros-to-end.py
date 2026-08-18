class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        k=nums.count(0)
        c=0
        if k==0:
            return 0
        else:
            for i in nums[-k:]:
                if i!=0:
                    c=c+1
        return c