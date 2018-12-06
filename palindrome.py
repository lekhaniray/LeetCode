class Solution:
    n = -12121
    def palindrome_check(n):
        pal = False
        
        if(n==0):
            pal = True
        if(n<0):
         
            pal = False
            
            
        if(n>0):
            copy=n
            n2=0
            while(n>0):
                rem = n%10

                n2 = n2*10+rem

                n=int(n/10)
                
            if(n2==copy):
                pal = True
                
            else:
                pal =False
                
        return(pal)
        
        
    ret = palindrome_check(n)
    print(ret)
                
            
        
            
