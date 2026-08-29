class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        frequency = {}

        for char in magazine:
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1

        for char in ransomNote:
            if char not in frequency:
                return False

            if frequency[char] == 0:
                return False

            frequency[char] -= 1

        return True
       