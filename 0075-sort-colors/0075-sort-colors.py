class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low=0 # refers to 0's only
        mid=0 # refers to current element
        high=len(nums)-1
        while mid<=high:
            if nums[mid]==0:
                # if cuurent ele is Zero means Swap with low
                nums[low],nums[mid]=nums[mid],nums[low]
                mid+=1
                low+=1
            elif nums[mid]==1:
                # if mid =1 means move mid one step
                mid+=1
            else:
                # if mid =2 meaans swap with high , high--
                nums[mid],nums[high]=nums[high],nums[mid]
                high-=1

