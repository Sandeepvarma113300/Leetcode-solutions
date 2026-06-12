class Solution:
    def reverseWords(self, s: str) -> str:
        words=s.split()
        for i in range(len(words)):
            j=list(words[i])
            p=0
            q=len(j)-1
            while p<q:
                j[p],j[q]=j[q],j[p]
                p=p+1
                q=q-1
            words[i]="".join(j)
        return " ".join(words)