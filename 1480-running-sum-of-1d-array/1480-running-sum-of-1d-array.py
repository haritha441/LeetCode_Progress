class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        a = 0
        b = []
        for num in nums:
            a = a + num
            b.append(a)
        return b

        