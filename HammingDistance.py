class Solution:
    def hammingDistance(x, y):
        A = [a for a in bin(x)][2:]
        B = [b for b in bin(y)][2:]
        length = max(len(A), len(B))
        dist = 0
        listz = [0]*(abs(len(A)-len(B)))
        if(len(A)>len(B)):
            B = listz + B

        else:
            A = listz + A

        for i in range(0, length):
            if(int(A[i]) != int(B[i])):
                dist += 1

        return(dist)

    x = 1
    y = 4
    ret = hammingDistance(x,y)
    print(ret)
