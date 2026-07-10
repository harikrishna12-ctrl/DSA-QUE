class Solution(object):
    def subarraySum(self, nums, k):
        #THIS WAS MY BRUTE FORCE APPROACH OK NOW WE ARE MOVING TO TE OPTIMAL
        # count = 0
        # n = len(nums)

        # for i in range(0,n):
        #     sums = 0
        #     for j in range(i,n):
        #         sums = sums + nums[j]
        #         if(sums == k):
        #             count = count + 1        
        # return count

        # IF YOU GET A SUB ARRAY QUESTION PREFIXSUM AND HASH IS THE ULTIMATE ANS OK
        count = 0
        prefixsum = 0
        hashi = {0:1}
        for num in nums:

            prefixsum = prefixsum + num
            if(prefixsum - k) in hashi:
                count = count + hashi[prefixsum - k]
            hashi[prefixsum] = hashi.get(prefixsum,0) + 1
        return count