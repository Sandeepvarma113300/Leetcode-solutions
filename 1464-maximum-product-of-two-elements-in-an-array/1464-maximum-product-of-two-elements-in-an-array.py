class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        maxx=nums[len(nums)-1]
        maxx2=nums[len(nums)-2]
        return ((maxx)-1)*((maxx2)-1)
