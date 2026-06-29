class Solution(object):
    def isPowerOfFour(self, n):
      s=n
      if n ==1:
        return True
      if(n == 0):
        return False
      else:
       while(n>1 and n %4 ==0):
        n = n//4
      if(n ==1 ):
        return True
      else: 
        return False
       