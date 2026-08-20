class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        arr = []
        arr.append(gain[0])
        for i in range(1, len(gain)):
            arr.append(gain[i] + arr[i-1])
        print(arr)
        m=0
        for k in arr:
            m=max(k,m)
        return m