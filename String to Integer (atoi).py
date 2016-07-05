class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if not str:
            return 0
        str = str.strip()
        match = re.search(r'\d+', str)
        if not match:
            return 0
        num = match.group()
        numStart = str.index(num)
        if numStart == 1 and str[0] != '+' and str[0] != '-':
            return 0
        if numStart > 1:
            return 0
        sign = 1 if numStart == 0 or str[numStart - 1] != '-' else -1
        num = int(num) * sign
        if num > 2147483647:
            return 2147483647
        if num < -2147483648:
            return -2147483648
        return num
