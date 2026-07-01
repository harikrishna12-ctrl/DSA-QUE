class Solution(object):
    def rotate(self, nums, k):
       #this is brute force approach
        # k = k % len(nums)
        
        # temp = []
        # for i in range(0,len(nums) - k):
        #     temp.append(nums[i])
        # j =0
        # for i in range(len(nums) - k ,len(nums)):
        #     nums[j] = nums[i]
        #     j = j + 1
        # for i in range(0,len(temp)):
        #     nums[k+i] = temp[i]
        # return nums
        k =k%len(nums)
        if k==0 :
            return nums
        k =k%len(nums)
        
        low =0 
        high = len(nums) -1
        mid = len(nums) - k - 1
        self.reversefunction(nums,low , mid)
        self.reversefunction(nums,mid+1,high)
        return self.reversefunction(nums,low,high)
    
    def reversefunction(self,nums,n,m):
        j=m

        for i in range(n,m+1):
            if(i>=j):
                break

            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp 
            j = j-1
