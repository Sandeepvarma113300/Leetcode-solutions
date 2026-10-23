class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        k=-1
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<nums[i+1]:
                k=i
                break
        if k!=-1:
            for j in range(len(nums)-1,k,-1):
                if nums[j]>nums[k]:
                    nums[j],nums[k]=nums[k],nums[j]
                    break
        nums[k+1:]=nums[k+1:][::-1]
        return nums
