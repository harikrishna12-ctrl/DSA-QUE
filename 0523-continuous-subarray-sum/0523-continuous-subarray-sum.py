class Solution(object):
    def checkSubarraySum(self, nums, k):
        n = len(nums)
        
        # for i in range(n-1):
        #     sums=nums[i]
        #     for j in range(i+1,n):
        #         sums = sums +nums[j]
        #         m = j - i +1
        #         if(sums%k==0 and m>=2 ):
        #            return True
        # return False
        prefix_sum = 0
        hashmap = {0: -1}

        for i in range(len(nums)):
            prefix_sum += nums[i]

            remainder = prefix_sum % k

            if remainder in hashmap:
                if i - hashmap[remainder] >= 2:
                    return True
            else:
                hashmap[remainder] = i

        return False