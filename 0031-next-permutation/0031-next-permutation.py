class Solution(object):
    def nextPermutation(self, nums):
        n = len(nums)

        # Step 1: Find the pivot
        index = -1
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                index = i
                break

        # Step 2: If no pivot, reverse the whole array
        if index == -1:
            i = 0
            j = n - 1
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
            return

        # Step 3: Find the next greater element from the right
        for i in range(n - 1, index, -1):
            if nums[i] > nums[index]:
                nums[i], nums[index] = nums[index], nums[i]
                break

        # Step 4: Reverse the suffix
        i = index + 1
        j = n - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1