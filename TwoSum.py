'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 '''

case1, target1 = [2,7,11,15], 9
case2, target2 = [3,2,4], 6
case3, target3 = [3,3], 6


# def TwoSum(nums: list, target:int):
#     #answer = num - target:
#     seen = dict()
#     for index,num in enumerate(nums):
#         seen[num] = index
#         if target - num in seen:
#             return index, seen[num]

# print(TwoSum(case2, target2))

def TwoSum(nums: list, target: int):
    seen = {}
    for i,v in enumerate(nums):
        if target - v in seen:
            return i, seen[target-v]
        seen[v] = i

print(TwoSum(case2, target2))