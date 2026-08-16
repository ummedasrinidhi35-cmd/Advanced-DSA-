#1408
from typing_extensions import List


nums=[1,2,3,4]
res = [0]*len(nums)
curr_sum = 0
for i in range(len(nums)):
    curr_sum += nums[i]
    res[i] = curr_sum
print(res)
#1991 #724 
from typing import List
def findMiddleIndex(nums: List[int]) -> int:
    total = sum(nums)
    left_sum = 0
    for i in range(len(nums)):
        right_sum = total - nums[i] - left_sum
        if left_sum == right_sum:
            return i
        left_sum += nums[i]
    return -1

        