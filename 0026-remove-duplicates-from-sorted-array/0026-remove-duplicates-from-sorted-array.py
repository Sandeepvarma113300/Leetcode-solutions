class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #pointer-technique for it
        i=0
        for j in range(1,len(nums)):
            if nums[j]!=nums[i]:
                nums[i+1]=nums[j]
                i=i+1
        return i+1