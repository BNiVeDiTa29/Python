class Solution:
    #code to reverse an array
    def reverseArray(self, nums: list[int]) -> None:
        # TODO
        

                i = 0
                j = len(nums)-1
                    
                while i<=j:

                        temp = nums[i]
                        nums[i] = nums[j]
                        nums[j] = temp

                        i=i+1
                        j = j-1
    pass
