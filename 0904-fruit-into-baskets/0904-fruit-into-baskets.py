class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left=0
        freq={}
        max_len=0
        for right in range(len(fruits)):
            if fruits[right] in freq:
                freq[fruits[right]]+=1
            else:
                freq[fruits[right]]=1
            while len(freq)>2:
                freq[fruits[left]]-=1
                if freq[fruits[left]] ==0:
                    del freq[fruits[left]]
                left=left+1
            current_length=right-left+1
            max_len=max(max_len,current_length)
        return max_len