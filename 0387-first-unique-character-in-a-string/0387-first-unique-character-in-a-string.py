class Solution:
    def firstUniqChar(self, s: str) -> int:
        frequency = {}
        for char in s:
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1

       
        for i in range(len(s)):
            if frequency[s[i]] == 1:
                return i

        return -1


