class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1:
            return 0
        p=1
        left=0
        c=0
        for right in range(len(nums)):
            p=p*nums[right]
            while p>=k:
                p//=nums[left]
                left=left+1
            c=c+(right-left+1)
        return c
