class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        m = 0

        for num in nums:
            m ^= num

        return m
        