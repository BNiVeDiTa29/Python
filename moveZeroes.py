#moving all the zeroes in a list to the end

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        # TODO
        i = 0

        for j in range(0, len(nums)):
            if nums[j] != 0:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                i=i+1
        pass
