class Solution(object):
    def majorityElement(self, nums):
       hash = {}
       n =len(nums)

       for num in nums:
        hash[num] =hash.get(num,0)+1
       
       for key in hash:
        if(hash[key]>n//2 ):
            return key