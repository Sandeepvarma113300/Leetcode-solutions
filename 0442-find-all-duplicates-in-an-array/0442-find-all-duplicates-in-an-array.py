from collections import Counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        s=Counter(nums)
        b=[]
        for i,j in s.items():
            if j==2:
                b.append(i)
        return b

        