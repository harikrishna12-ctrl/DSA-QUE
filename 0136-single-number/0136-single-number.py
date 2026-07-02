class Solution(object):
    def singleNumber(self, nums):
        hash ={}
        n = len(nums)
        for num in nums:
            hash[num] = hash.get(num,0) + 1
        
        for key in hash:
            if(hash[key]==1):
                return key
        