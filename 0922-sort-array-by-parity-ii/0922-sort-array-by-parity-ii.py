class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        b=[0]*len(nums)
        p=0
        n=1
        for i in nums:
            if i%2==0:
                b[p]=i
                p=p+2
            else:
                b[n]=i
                n=n+2
        return b