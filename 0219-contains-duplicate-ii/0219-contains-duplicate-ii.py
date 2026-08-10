class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        n =len(nums)

        # for i in range(0,n-1):
        #    for j in range(i+1,n):
        #      if(nums[i]==nums[j] and abs(i-j)<=k):
        #          return True
        #          break
        # return False

        hashi ={}

        for i in range(n):
            if nums[i] in hashi:
                if i -hashi[nums[i]]<=k:
                    return True

            hashi[nums[i]] = i
        return False
        