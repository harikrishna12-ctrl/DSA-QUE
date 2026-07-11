class Solution(object):
    def getRow(self, rowIndex):
        n = rowIndex
        res = 1
        r = n+1
        ans = []
        if(n == 0):
         ans.append(1)
         return ans
        else:
            ans.append(1)
            for i in range(r-2):
             res = res* (n -i)
             res = res//(i+1)
             ans.append(res)
            ans.append(1)
            return ans

        