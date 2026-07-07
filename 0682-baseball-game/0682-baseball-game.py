class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        for i in range(len(operations)):
            if operations[i]=="+":
                l=stack[-1]
                r=stack[-2]
                stack.append(l+r)
            elif operations[i]=="C":
                stack.pop()
            elif operations[i]=="D":
                p=stack[-1]
                stack.append(p*2)
            else:
                stack.append(int(operations[i]))
        return sum(stack)