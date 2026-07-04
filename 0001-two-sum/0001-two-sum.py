class Solution(object):
    def twoSum(self, nums, target):
    #   ans =[]
    #   for i in range(len(nums)):
    #     for j in range(len(nums)-1,-1,-1):
    #         if(i==j):
    #             pass
    #         else:
    #             if(nums[i]+nums[j] ==target):
    #                 ans.append(i)
    #                 ans.append(j)
    #                 break
    #     if(len(ans)==2):
    #         break
    #   return ans
      hash ={}
      i =0
      remaining = 0
      n = len(nums)
      for i in range(n):
        remaining = target - nums[i]

        if remaining in hash:
            return i, hash[remaining]
        if remaining not in hash:
            hash[nums[i]] = i