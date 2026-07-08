class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        pairs={
            "(":")",
            "{":"}",
            "[":"]"
        }
        for i in s:
            if i in "({[":
                stack.append(i)
            else:
                if len(stack)==0:
                    return False
                if pairs[stack[-1]]==i:
                    stack.pop()
                else:
                    return False
        return len(stack)==0