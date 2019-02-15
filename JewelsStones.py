class Solution1:

    def numJewelsInStones(J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        J = list(J)
        S = list(S)
        K = []
        for ele in S:
            if ele in J:
                K.append(ele)
                
        distinct = len(K)
        return(distinct)
    

