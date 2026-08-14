class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        m = 1
        p = 0

        while n > 0:
            digit = n % 10
            m *= digit
            p += digit
            n //= 10

        return m - p

        