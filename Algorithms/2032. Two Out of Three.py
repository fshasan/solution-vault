class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        res = nums1 + nums2 + nums3
        res = list(set(res))
        final_res = []

        for i in range(len(res)):
            if (
                (res[i] in nums1 and res[i] in nums2)
                or (res[i] in nums2 and res[i] in nums3)
                or (res[i] in nums3 and res[i] in nums1)
            ):
                final_res.append(res[i])

        return final_res
