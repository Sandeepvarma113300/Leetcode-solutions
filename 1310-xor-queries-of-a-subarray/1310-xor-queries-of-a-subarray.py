class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        p=[0]*len(arr)
        p[0]=arr[0]
        for i in range(1, len(arr)):
            p[i] = arr[i] ^ p[i-1]
        ans=[]
        for i,j in queries:
            if i==0:
                ans.append(p[j])
            else:
                ans.append(p[j]^p[i-1])
        return ans