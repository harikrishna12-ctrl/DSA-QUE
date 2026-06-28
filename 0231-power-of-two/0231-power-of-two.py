class Solution(object):
    def isPowerOfTwo(self, n):
        s=n
        if n ==0 :
            return False
        else :
            while(n%2==0):
                n=n//2
            return n==1
            
            if(n==1):
                return True
            else:
                return False