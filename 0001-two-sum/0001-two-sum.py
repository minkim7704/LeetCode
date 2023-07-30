'''
1. nums[0]: 다 더 해보면서 target 값 나오는지 확인
2. 타겟값 나오면 인덱스 리턴
'''

class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if i != j:
                    if nums[i] + nums[j] == target:
                        return i, j
        
        
        