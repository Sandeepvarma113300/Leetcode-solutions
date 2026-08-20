class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        res=[]
        res.append(sum(nums[1:len(nums)]))
        for i in range(1,len(nums)):
            left=sum(nums[0:i-1+1])
            sub=sum(nums[i+1:len(nums)])
            res.append(abs(sub-left))
        return res