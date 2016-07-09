dic = [' ', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        
        res = []
        getComb(digits, 0, res, '')
        return res

def getComb(digits, pos, res, cur):
    if pos >= len(digits):
        res.append(cur)
        return
    d = dic[int(digits[pos])]
    for i in range(0, len(d)):
        curCopy = cur[0:]
        curCopy += d[i]
        getComb(digits, pos + 1, res, curCopy)
        
