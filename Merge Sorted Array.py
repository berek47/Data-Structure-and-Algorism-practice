class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        a=len(nums1)-m
        for i in range(a):
            nums1.remove(nums1[-1])
        b=len(nums2)-n
        for i in range(b):
            nums2.remove(nums2[-1])
        nums1.extend(nums2)
        nums1.sort()
        return nums1
