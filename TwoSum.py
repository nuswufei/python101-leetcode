class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i in range(0, len(nums)):
            if (target - nums[i]) in dic:
                return [dic[target - nums[i]], i]
            else:
                dic[nums[i]] = i
        return []
              
