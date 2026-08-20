class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        p=0
        m=0
        for i in range(len(gain)):
            p=p+gain[i]
            m=max(p,m)
        return m