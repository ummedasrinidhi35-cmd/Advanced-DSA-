#930
from typing import List
def numSubarraysWithSum(nums: List[int], goal: int) -> int:
    def sub_arr(k):
        if k < 0:
            return 0
        left = 0
        count = 0
        curr_sum = 0
        for right in range(len(nums)):
            curr_sum += nums[right]
            while curr_sum > k:
                curr_sum -= nums[left]
                left += 1
            count += (right - left + 1)
        return count
    return sub_arr(goal) - sub_arr(goal - 1)
nums = [0,0,0,0,0]
goal = 0
print(numSubarraysWithSum(nums, goal))
#1248

def numberOfSubarrays(nums: List[int], k: int) -> int:
    def sub_arr(target):
        if target < 0:
            return 0
        left,count,odd = 0, 0, 0
        for right in range(len(nums)):
            if nums[right] % 2 == 1:
                odd += 1
            while odd > target:
                if nums[left] % 2 == 1:
                    odd -= 1
                left += 1
            count += (right - left + 1)
        return count
    return sub_arr(k) - sub_arr(k-1)
nums = [1,1,2,1,1]
Result = 3
print(numberOfSubarrays(nums, Result))
#1763

def longestNiceSubstring(s: str) -> str:
    if len(s) < 2:
        return ""
    uniq = set(s)
    for i,ch in enumerate(s):
        if ch.lower() in uniq and ch.upper() in uniq:
            continue
        left_str = longestNiceSubstring(s[:i])
        right_str = longestNiceSubstring(s[i+1:])

    
        return left_str if len(left_str) >= len(right_str) else right_str
    return s
s1="YazaAay"
s2="Bb"
s3="c"
print(longestNiceSubstring(s1))
print(longestNiceSubstring(s2))
print(longestNiceSubstring(s3))
