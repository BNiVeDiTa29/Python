#code to find the maximum and minimum values in an array

class Solution:
    def maxMin(self, nums: list[int]) -> tuple[int, int]:
        # TODO
        max_val = nums[0]
        for val in nums:
            if val > max_val:
                max_val = val

        min_val = nums[0]

        for valu in nums:
            if valu < min_val:
                min_val = valu

        return (max_val, min_val)
