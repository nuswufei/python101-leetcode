class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x < 10:
            return True
        leftDiv = 10 ** int(math.log10(x))
        rightDiv = 1
        while leftDiv > rightDiv:
            if x / leftDiv % 10 != x / rightDiv % 10:
                return False
            leftDiv /= 10
            rightDiv *= 10
        return True
