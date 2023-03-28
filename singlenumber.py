case1 = [2,2,1]
case2 = [4,1,2,1,2]
case3 = [1]

def singleNumber(nums: list) -> int:
    seen = {}
    for num in nums:
        if num in seen:
            seen[num] += 1
        else:
            seen[num] = 1
    
    for key, value in seen.items():
        if value == 1:
            return key

print(singleNumber(case2))
