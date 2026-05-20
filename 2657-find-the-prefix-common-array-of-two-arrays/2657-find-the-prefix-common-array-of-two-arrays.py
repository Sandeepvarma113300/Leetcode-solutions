class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        s1=set()
        s2=set()
        res=[]
        for i in range(len(A)):
            s1.add(A[i])
            s2.add(B[i])
            c=0
            for n in s1:
                if n in s2:
                    c=c+1
            res.append(c)
        return res