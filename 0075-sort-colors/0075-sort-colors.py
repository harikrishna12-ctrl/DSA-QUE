class Solution(object):
    def sortColors(self, nums):
        ans0 =[]
        ans1 =[]
        ans2 = []

        for i in range(len(nums)):
            if(nums[i] == 0):
                ans0.append(nums[i])
            if(nums[i] == 1):
                ans1.append(nums[i])
            if(nums[i]==2):
                ans2.append(nums[i])

        for i in range(len(ans0)):
            nums[i] = ans0[i]
        for i in range(len(ans0),len(ans0) + len(ans1)):
            nums[i] = ans1[i -len(ans0)]
        for i in range(len(ans0)+ len(ans1), len(ans0)+ len(ans1)+len(ans2)):
            nums[i] = ans2[i-len(ans1)-len(ans0)]

        return nums