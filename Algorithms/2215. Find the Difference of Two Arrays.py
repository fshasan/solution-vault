class Solution(object):
    def findDifference(self, nums1, nums2):
        nums_1 = []
        nums_2 = []

        for i in nums1:
            if i not in nums2 and i not in nums_1:
                nums_1.append(i)
        for i in nums2:
            if i not in nums1 and i not in nums_2:
                nums_2.append(i)

        return [nums_1, nums_2]
        