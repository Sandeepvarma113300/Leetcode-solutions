class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        window=sum(arr[:k])
        c=0
        if window//k>=threshold:
            c=c+1
        for i in range(k,len(arr)):
            window=window-arr[i-k]+arr[i]
            avg=window//k
            if avg>=threshold:
                c=c+1
        return c

