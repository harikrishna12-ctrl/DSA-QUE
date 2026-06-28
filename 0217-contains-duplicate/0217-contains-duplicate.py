class Solution(object):
    def containsDuplicate(self, nums):
       
       hash = {}

       for num in nums:
        hash[num] = hash.get(num,0) +1

       for keys in hash:
         if(hash[keys]>1):
            return True
        
       return False