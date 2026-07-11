class Solution(object):

    def ncrs(self, n, r):
        res = 1

        for i in range(r):
            res = res * (n - i)
            res = res // (i + 1)

        return res

    def generate(self, numRows):
        ans = []

        for i in range(numRows):
            temp = []

            for j in range(i + 1):
                temp.append(self.ncrs(i, j))

            ans.append(temp)

        return ans