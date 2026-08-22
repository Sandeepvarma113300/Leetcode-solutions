class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s=0
        p=1
        temp=n
        f=0
        while temp!=0:
            r=temp%10
            s=s+r
            p=p*r
            temp=temp//10
        f=s+p
        if n%f==0:
            return True
        else:
            return False