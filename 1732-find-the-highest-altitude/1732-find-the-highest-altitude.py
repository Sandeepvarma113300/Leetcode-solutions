class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        high=0
        s=0
        for i in range(len(gain)):
            s=s+gain[i]
            high=max(s,high)
        return high