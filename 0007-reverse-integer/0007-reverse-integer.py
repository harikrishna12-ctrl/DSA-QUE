class Solution(object):
    def reverse(self, x):
       sign=0
       reversenum=0
       lastdigit=0
       if(x<0):
        sign = -1
       else:
         sign=1
       x=abs(x)
       while(x!=0):
        lastdigit=x%10
        reversenum = reversenum *10 + lastdigit
        x = x//10
       thenum = reversenum * sign
       if thenum< -2**31 or thenum>2**31:
        return 0
       else:
        return thenum
