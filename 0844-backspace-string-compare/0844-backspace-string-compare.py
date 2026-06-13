class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def final(string):
            stack=[]
            for i in string:
                if i=="#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(i)
            return "".join(stack)
        return final(s)==final(t)