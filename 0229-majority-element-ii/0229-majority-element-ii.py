class Solution(object):
    def majorityElement(self, nums):
       hash = {}
       ans = []
       max= 0
       n = len(nums)
       for num in nums:
        hash[num] = hash.get(num,0)+1
     
       for key in hash:
         if(hash[key]> len(nums)//3 ):
            ans.append(key)
       return ans