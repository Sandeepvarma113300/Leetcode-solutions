class Solution(object):
    def moveZeroes(self, nums):
        b=[]
        for i in range(len(nums)):
            if nums[i]!=0:
                b.append(nums[i])
        for i in range(len(b)):
            nums[i]=b[i]
        for i in range(len(b),len(nums)):
            nums[i]=0