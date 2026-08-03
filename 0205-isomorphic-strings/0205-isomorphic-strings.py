class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_freq = {}
        t_freq = {}

        for i in range(len(s)):
            ch1 = s[i]
            ch2 = t[i]

           
            if ch1 in s_freq:
                if s_freq[ch1] != ch2:
                    return False
            else:
                s_freq[ch1] = ch2

           
            if ch2 in t_freq:
                if t_freq[ch2] != ch1:
                    return False
            else:
                t_freq[ch2] = ch1

        return True