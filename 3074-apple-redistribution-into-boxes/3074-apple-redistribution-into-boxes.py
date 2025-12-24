class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        s=sum(apple)
        x=0
        c = sorted(capacity, reverse=True)
        for i in c:
            s=s-i
            x=x+1
            if s<=0:
                break
        return x