class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        res = 0
        dif = sys.maxint
        i1 = 0
        while i1 < len(nums) - 2:
            i2 = i1 + 1
            i3 = len(nums) - 1
            while i2 < i3:
                sum = nums[i1] + nums[i2] + nums[i3]
                d = abs(sum - target)
                if d < dif:
                    res = sum
                    dif = d
                if sum < target:
                    i2 += 1
                elif sum > target:
                    i3 -= 1
                else:
                    return sum
            i1 += 1
        return res
