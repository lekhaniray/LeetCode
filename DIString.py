import random

class Solution:
    S = "DIDIDI"
    def diStringMatch(S):
        a = 4
        print(S)
        listnew = [a]
        S = list(S)
        print(S)
        for ele in S:
            x = random.randint(1,9)
            if(ele == "I"):
                a += x
                
            elif(ele == "D"):
                a -= x
                
            listnew.append(a)
        print(listnew)    
        return(listnew)
        
    ret = diStringMatch(S)
    print(ret)

                
        
