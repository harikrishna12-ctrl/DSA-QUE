class Solution(object):
    def rotate(self, nums, k):
       
        k = k % len(nums)
        
        temp = []
        for i in range(0,len(nums) - k):
            temp.append(nums[i])
        j =0
        for i in range(len(nums) - k ,len(nums)):
            nums[j] = nums[i]
            j = j + 1
        for i in range(0,len(temp)):
            nums[k+i] = temp[i]
        return nums
        
        