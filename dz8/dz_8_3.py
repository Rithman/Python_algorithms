class Solution:
    def removeDuplicates(self, nums):
        length = len(nums)
        p1 = 0
        p2 = 0
        while p1 < length:

            if nums[p1] != nums[p2]:
                p2 += 1
                nums[p2] = nums[p1]
            p1 += 1

        return p2 + 1
