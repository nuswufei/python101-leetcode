class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        res = strs[0]
        for s in strs:
            res = longestPrefix(res, s)
        return res

def longestPrefix(str1, str2):
    if len(str1) == 0 or len(str2) == 0:
        return ''
    i = 0
    while i < len(str1) and i < len(str2) and str1[i] == str2[i]:
        i += 1
    return str1[:i]
