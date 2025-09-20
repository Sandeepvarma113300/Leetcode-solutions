class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False

        map_p_s = {}
        map_s_p = {}

        for i in range(len(pattern)):
            p = pattern[i]
            w = words[i]

           
            if p in map_p_s:
                if map_p_s[p] != w:
                    return False
            else:
                map_p_s[p] = w

       
            if w in map_s_p:
                if map_s_p[w] != p:
                    return False
            else:
                map_s_p[w] = p

        return True
