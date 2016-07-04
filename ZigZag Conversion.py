class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if (numRows == 1):
            return s
        result = []
        for row in range(0, numRows):
            i = 0
            while i < len(s):
                if i + row < len(s):
                    result.append(s[i + row])
                if row != 0 and row != numRows - 1 and i + numRows * 2 - 2 - row < len(s):
                    result.append(s[i + numRows * 2 - 2 - row])
                i += numRows * 2 - 2
        return ''.join(result)
