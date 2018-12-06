class Solution:
    n=-345
    def reverse1(n):
        
        if(n>0):
            copy=0
            rem=0
            while(n> 0):
                
                rem = n%10
                copy=copy*10 + rem
                n=int(n/10)
                
        if(n<0):
            n = abs(n)
            copy=0
            rem=0
            while(n> 0):
                
                rem = n%10
                copy=copy*10 + rem
                n=int(n/10)
                
            copy = -copy
                
                
        return(copy)
            
            
    ret = reverse1(n)
    print(ret)
                
                
                
        
        
   

        
            
