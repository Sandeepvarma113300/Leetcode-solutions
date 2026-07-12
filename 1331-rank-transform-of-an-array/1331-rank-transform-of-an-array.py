class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        n=sorted(arr)
        r=1
        freq={}
        for i in n:
            if i not in freq:
                freq[i]=r
                r=r+1
        b=[]
        for i in arr:
            b.append(freq[i])
        return b
