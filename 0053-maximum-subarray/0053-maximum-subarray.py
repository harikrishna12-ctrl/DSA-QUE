class Solution(object):
    def maxSubArray(self, nums):
        maxi = -343434343
        n = len(nums)
        sums = 0 
        for i in range(n):
            sums = sums + nums[i]
            if(sums>maxi):
                maxi = sums
            
            if(sums<0 and nums[i]<0):
                sums = 0

        return maxi
        
        