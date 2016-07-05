class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 0;
        sign = 1 if x >= 0 else -1
        x = abs(x)
        while x != 0:
            res *= 10
            res += x % 10
            x /= 10
        res *= sign
        return 0 if res < -2 ** 31 or res > 2 ** 31 - 1 else res
