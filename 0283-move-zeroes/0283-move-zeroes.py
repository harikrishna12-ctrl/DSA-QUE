class Solution(object):
    def moveZeroes(self, nums):
        j = -1
        for i in range(0, len(nums)):
            if(nums[i] == 0):
                j = i
                break
        if(j == -1):
            return nums
        else:
         for i in range(j+1, len(nums)):
            if(nums[i] != 0 ):
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp 
                j = j +1
            
         return nums