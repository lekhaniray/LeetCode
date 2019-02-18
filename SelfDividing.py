class Solution:
    def selfDividingNumbers(left, right):
        sdnList = []
        for i in range(left, right+1):
            add = 'True'
            copy = i
            l = str(i)
            l = list(l)
            if('0' in l):
                continue

            for x in l:
                if(copy % int(x) != 0):
                    add = 'False'

            if(add == 'True'):
                sdnList.append(i)

        print(sdnList)

    left = 1
    right = 22
    ret = selfDividingNumbers(left, right)
