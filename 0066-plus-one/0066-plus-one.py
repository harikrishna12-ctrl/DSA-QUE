class Solution(object) :
    def plusOne(self, digits):
        # nums = digits
        # n = len(digits)
        # num =0
        # j = n-1
        # rev =0
        # for i in range(0,n):
        #     num = digits[i]* (10**j)
        #     rev = rev + num
        #     j = j-1
        # rev = rev +1
        # s= rev
        
        
        # z =n-1
        # while(rev>0):
        #     dig = rev%10
        #     digits[z]=dig
        #     z = z -1
        #     rev = rev//10
        # if(s%10==0 and s!=0):
        #    digits.append(0)
        # return digits

     
        n = len(digits)

        # Traverse from the last digit
        for i in range(n - 1, -1, -1):

            # If digit is less than 9, just add 1 and return
            if digits[i] < 9:
                digits[i] += 1
                return digits

            # If digit is 9, make it 0 and carry
            digits[i] = 0

        # If all digits were 9, add 1 at the beginning
        return [1] + digits