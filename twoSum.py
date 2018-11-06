class Solution:
    nums = [2, 7, 11, 15]
    target = 18
    
    def twoSum(nums, target):
        copy = target
        l = len(nums)
        answer = []
        for i in range(0, l):
            copy = target - nums[i]
            for j in range(0,l):
                if(j == i):
                    continue
                if(nums[j] == copy):
                    answer.append(nums[i])
                    answer.append(nums[j])
                    return(answer)
        
        
        
    ret = twoSum(nums, target)
    print(ret)
        
