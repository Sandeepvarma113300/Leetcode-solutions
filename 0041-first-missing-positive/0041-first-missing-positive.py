from collections import Counter
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n=len(nums)
        b=Counter(nums)
        ans=float('inf')
        mx=max(nums)
        c=1
        for i in range(1,mx+1):
            if i in b:
                c=c+1
            else:
                if i>0:
                    ans=min(ans,i)
                    return ans
        return c