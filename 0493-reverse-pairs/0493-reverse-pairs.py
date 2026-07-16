class Solution(object):
    def reversePairs(self, nums):
        count = [0]

        def mergeSort(arr, low, high):
            if low >= high:
                return

            mid = (low + high) // 2

            mergeSort(arr, low, mid)
            mergeSort(arr, mid + 1, high)

            merge(arr, low, mid, high)

        def merge(arr, low, mid, high):
            j = mid + 1

            # Count reverse pairs
            for i in range(low, mid + 1):
                while j <= high and arr[i] > 2 * arr[j]:
                    j += 1
                count[0] += j - (mid + 1)

            temp = []
            left = low
            right = mid + 1

            while left <= mid and right <= high:
                if arr[left] <= arr[right]:
                    temp.append(arr[left])
                    left += 1
                else:
                    temp.append(arr[right])
                    right += 1

            while left <= mid:
                temp.append(arr[left])
                left += 1

            while right <= high:
                temp.append(arr[right])
                right += 1

            for i in range(low, high + 1):
                arr[i] = temp[i - low]

        mergeSort(nums, 0, len(nums) - 1)
        return count[0]