#1408
from typing_extensions import List


nums=[1,2,3,4]
res = [0]*len(nums)
curr_sum = 0
for i in range(len(nums)):
    curr_sum += nums[i]
    res[i] = curr_sum
print(res)
#1732
from typing import List

        