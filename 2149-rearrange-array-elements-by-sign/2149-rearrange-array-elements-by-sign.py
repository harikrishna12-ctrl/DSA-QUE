class Solution(object):
    def rearrangeArray(self, nums):
       n = len(nums)
       z = 1
       j = 0 
       zums = [0] * n
       for i in range(n):

        if(nums[i]>0 ):
            zums[j] = nums[i]
            j = j +2
        else:
            zums[z] = nums[i]
            z= z+2
       for i in range(0,len(zums)):
        nums[i] = zums[i]
        
       return nums        