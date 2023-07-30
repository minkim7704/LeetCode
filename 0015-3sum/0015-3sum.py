'''
1. nums = [정수 배열]
2. new array = [ [i + j + k = 0] ... ]
3. i != j != k

일단 nums[0] 넣어
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # -4 -1 -1 0 1 2
        answer = set()
        
        for i in range(len(nums)-2):
            # 0번 자리에 있는 수부터 시작한다.
            j = i+1
            k = len(nums)-1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    answer.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
        return answer