class Solution(object):
    def largestPerimeter(self, nums):
        nums.sort(reverse=True)  # sort in descending order
        for i in range(len(nums) - 2):
            if nums[i] < nums[i+1] + nums[i+2]:  # triangle condition
                return nums[i] + nums[i+1] + nums[i+2]
        return 0