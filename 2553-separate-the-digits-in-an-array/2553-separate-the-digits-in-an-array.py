class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        b=[]
        for i in nums:
            for j in str(i):
                b.append(int(j))
        return b
