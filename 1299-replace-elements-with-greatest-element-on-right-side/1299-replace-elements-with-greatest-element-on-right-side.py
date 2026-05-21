class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        b=[]
        maxele=-1
        for i in range(len(arr)-1,-1,-1):
            b.append(maxele)
            if arr[i]>maxele:
                maxele=arr[i]
        return b[::-1]