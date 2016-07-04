class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        totalLen = len(nums1) + len(nums2)
        if totalLen & 1 == 1:
            return findKth(nums1, nums2, 0, 0, totalLen // 2)
        else:
            return (findKth(nums1, nums2, 0, 0, totalLen / 2 - 1) + findKth(nums1, nums2, 0, 0, totalLen / 2)) / 2.0
    
def findKth(nums1, nums2, start1, start2, k):
    if len(nums1) - start1 > len(nums2) - start2:
        return findKth(nums2, nums1, start2, start1, k)
    if start1 >= len(nums1):
        return nums2[start2 + k]
    if k == 0:
        return min(nums1[start1], nums2[start2])
    head1 = min(len(nums1) - 1 - start1, (k - 1) // 2)
    head2 = k - 1 - head1
    if nums1[start1 + head1] > nums2[start2 + head2]:
        return findKth(nums1, nums2, start1, start2 + head2 + 1, k - head2 - 1)
    else:
        return findKth(nums1, nums2, start1 + head1 + 1, start2, k - head1 - 1)
