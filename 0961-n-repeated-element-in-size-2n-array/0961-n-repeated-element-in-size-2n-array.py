from collections import Counter
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n=Counter(nums)
        for i,j in n.items():
            if j>=2:
                return i
    