class Solution(object):
    def twoSum(self, nums, target):
      ans =[]
      for i in range(len(nums)):
        for j in range(len(nums)-1,-1,-1):
            if(i==j):
                pass
            else:
                if(nums[i]+nums[j] ==target):
                    ans.append(i)
                    ans.append(j)
                    break
        if(len(ans)==2):
            break
      return ans
        