class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n=0
        m=0
        for i in num1:
            n=n*10+ord(i)-48
        for i in num2:
            m=m*10+ord(i)-48
        res=n*m
        return f"{res}"