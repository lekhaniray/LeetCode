class Solution:
    def flipAndInvertImage(A):
        length = len(A)
        print(A)
        for item in A:
            item.reverse()


        B = []

        for ele in A:
            newList = [1-x for x in ele]
            B.append(newList)
            print(B)






        print(B)
        return(B)

    A = [[1,1,0], [1,0,0], [1,1,1]]
    ret = flipAndInvertImage(A)
    print(ret)
