class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack=[]
        b=[]
        for i in range(1,n+1):
            if i in target:
                b.append(i)
                stack.append("Push")
            else:
                b.append(i)
                stack.append("Push")
                b.pop()
                stack.append("Pop")
            if b==target:
                return stack
                

            