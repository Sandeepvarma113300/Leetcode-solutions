class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        ans=0
        while l<r:
            h=min(height[l],height[r])
            a=(r-l)*h
            ans=max(a,ans)
            if height[l]<height[r]:
                l=l+1
            else:
                r=r-1
        return ans
