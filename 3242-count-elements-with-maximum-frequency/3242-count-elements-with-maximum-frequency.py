from collections import Counter
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        a=Counter(nums)
        am=max(Counter(a.values()))
        return sum(i for i in a.values() if i==am)
    