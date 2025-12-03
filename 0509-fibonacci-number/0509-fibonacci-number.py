class Solution:
    def fib(self, n: int) -> int:
        def f(i):
            if i <= 1:
                return i
            return f(i-1) + f(i-2)

        return f(n)
