class Solution:
    def judgeCircle(moves):
        """
        :type moves: str
        :rtype: bool
        """
        x=0
        y=0

        for move in moves:
            print(move)
            if(move == 'U'):
                y = y+1
            if(move == 'D'):
                y = y-1
            if(move == 'L'):
                x = x-1
            if(move == 'R'):
                x = x+1
            print(x,y)



        if(x==0 and y==0):
            output = True
        else:
            output = False

        return(output)
    moves = 'DURDLDRRLL'
    ret = judgeCircle(moves)
    print(ret)
