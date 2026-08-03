class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left=0
        freq={}
        k=2
        mx=0
        for i in range(len(fruits)):
            if fruits[i] in freq:
                freq[fruits[i]]+=1
            else:
                freq[fruits[i]]=1
            while len(freq)>k:
                freq[fruits[left]]-=1
                if freq[fruits[left]]==0:
                    del freq[fruits[left]]
                left=left+1
            curr=i-left+1
            mx=max(mx,curr)
        return mx