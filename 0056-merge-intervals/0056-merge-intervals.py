class Solution(object):
    def merge(self, intervals):
        n = len(intervals)
        lists = sorted(intervals)
        ans =[]
        first =lists[0][0]
        med =lists[0][0]
        for i in range(0,n):
            
           
            if(med>=lists[i][0]):
                med =max(med,lists[i][1])
            else:
                ans.append([first,med])
                first =lists[i][0]
                med =lists[i][1]
                
        ans.append([first, med])     
        return ans