class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        b=[]
        d=[]
        res=[]
        for i in range(len(nums)):
            if nums[i]>0:
                b.append(nums[i])
            else:
                d.append(nums[i])
        p=0
        q=0
        while p<len(b) and q <len(d):
            res.append(b[p])
            res.append(d[q])
            p=p+1
            q=q+1
        return res