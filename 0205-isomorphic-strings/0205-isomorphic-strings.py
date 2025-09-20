class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_s_t = {}
        map_t_s = {}
        
        for i in range(len(s)):
            ch_s = s[i]
            ch_t = t[i]
            if ch_s in map_s_t:
                if map_s_t[ch_s] != ch_t:   
                    return False
            else:
                map_s_t[ch_s] = ch_t  
            if ch_t in map_t_s:
                if map_t_s[ch_t] != ch_s:  
                    return False
            else:
                map_t_s[ch_t] = ch_s   

        return True
