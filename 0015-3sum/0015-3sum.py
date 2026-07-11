class Solution(object):
    def threeSum(self, nums):
     # this is my brute force upproach  
    #  n = len(nums)
    #    temp =[]
    #    for i in range(0,n-2):
    #     for j in range(i+1,n-1):
    #         ans = []
    #         for z in range(j+1,n):
    #             if(nums[i] + nums[j] + nums[z] == 0) :
    #                 triplet = sorted([nums[i], nums[j], nums[z]])
    #                 if triplet not in temp:
    #                     temp.append(triplet)
    #    return temp
    #  ans= []
    #  z =0
    #  hashi ={}
    #  n = len(nums)
    
    #  for i in range(0,n):
    #     hashi ={}
    #     for j in range(i+1,n):
    #         third = -(nums[i]+nums[j])
    #         if third in hashi:
    #             temp = sorted([nums[i],nums[j],third])
    #             if temp not in ans:
    #                 ans.append(temp)
    #         hashi[nums[j]] =1
    #  return ans
   
        nums.sort()
        n = len(nums)
        ans = []

        for i in range(n):
            # Skip duplicate first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = n - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total < 0:
                    j += 1

                elif total > 0:
                    k -= 1

                else:
                    ans.append([nums[i], nums[j], nums[k]])

                    j += 1
                    k -= 1

                    # Skip duplicate second element
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                    # Skip duplicate third element
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

        return ans
