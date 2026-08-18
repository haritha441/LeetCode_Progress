class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        n = s.split()
        p = n[-1]
        m = len(p)
        return(m)
        