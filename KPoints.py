import math
class Solution:
    points = [[1, 2], [2, 2]]
    K = 1
    def kClosest(points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        dist = 0
        distList = []
        pointList = []
        for ele in points:
            dist = math.sqrt(ele[0]**2 + ele[1]**2)
            distList.append(dist)

        for i in range(0, K):
            min = 100
            for ele1 in distList:
                if(ele1<min):
                    min1 = ele1

            pos = distList.index(min1)
            pointList.append(points[pos])

        print(pointList)

    ret = kClosest(points, K)
    print(ret)
