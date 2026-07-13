class Solution(object):
    def fourSum(self, nums, target):
        # n = len(nums)
        # ans =[]
        # for i in range(n-3):
        #     for j in range(i+1,n-2):
        #         for k in range(j+1,n-1):
        #             for z in range(k+1,n):
        #                 d =nums[i]+nums[j]+nums[k]+nums[z]
        #                 y =sorted([nums[i],nums[j],nums[k],nums[z]])
        #                 if(d== target and y not in ans):
        #                    ans.append(y)
        # return ans

        n =len(nums)
        ans=[]
        s =set()
        for i in range(n-2):
            for j in range(i+1,n-1):
                hashi ={}
                for k in range(j+1,n):
                    forth = target -(nums[i]+nums[j]+nums[k])
                    if forth in hashi:
                      temp =sorted([nums[i],nums[j],nums[k],forth])
                      s.add(tuple(temp))
                    hashi[nums[k]] =1
        return [list(x) for x in s]