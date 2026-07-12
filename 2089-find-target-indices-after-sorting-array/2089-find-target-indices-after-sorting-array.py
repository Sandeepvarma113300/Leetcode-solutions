class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        n=sorted(nums)
        b=[]
        for i in range(len(n)):
            if n[i]==target:
                b.append(i)
        return b