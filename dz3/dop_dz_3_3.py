class Solution(object):
    def containsDuplicate(self, nums):
        self.nums = nums
        my_set = set()
        for i in range(len(self.nums)):
            if self.nums[i] in my_set:
                return True
            elif self.nums[i] not in my_set:
                my_set.add(self.nums[i])
                if i == len(self.nums) - 1:
                    return False
