class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        b=[]
        freq={}
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        for k,v in freq.items():
            if v==2:
                b.append(k)
                
        return b