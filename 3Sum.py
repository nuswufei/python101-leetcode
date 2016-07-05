class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        res = []
        i1 = 0
        while i1 < len(nums) - 2:
            i2 = i1 + 1
            i3 = len(nums) - 1
            while i2 < i3:
                sum = nums[i1] + nums[i2] + nums[i3]
                if sum == 0:
                    res.append([nums[i1], nums[i2], nums[i3]])
                    i2 = incre(nums, i2)
                    i3 = decre(nums, i3)
                elif sum > 0:
                    i3 = decre(nums, i3)
                else:
                    i2 = incre(nums, i2)
            i1 = incre(nums, i1)
        return res

def incre(nums, i):
    n = nums[i]
    while i < len(nums) and nums[i] == n:
        i += 1
    return i

def decre(nums, i):
    n = nums[i]
    while i >= 0 and nums[i] == n:
        i -= 1
    return i
            
