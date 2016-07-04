class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if (len(s) <= 1):
            return len(s)
        left = 0
        right = 1
        window = set(s[0])
        result = 1
        while right < len(s):
            if s[right] in window:
                result = max(result, right - left)
                while s[left] != s[right]:
                    window.remove(s[left])
                    left += 1
                left += 1
            else:
                window.add(s[right])
            right += 1
        result = max(right - left, result)
        return result
        
