class Solution(object):
    def missingNumber(self, nums):
       # this was my brute force approach abi me accha solutiom dundke lahunga ruko

        # n = len(nums)
        # count = 0
        # for i in range(0,n+1):
        #     for j in range(0,n):
        #         if(nums[j] == i):
        #             count = count+1
        #             break
        #     if(count != i+1):
        #         return i
      
      n = len(nums)
      hash = {}
      for i in range(0 , n+1):
        hash[i] = 0

      for x in nums:
        hash[x] = 1
      for key in hash:
        if(hash[key] == 0):
           return key
     
        
 