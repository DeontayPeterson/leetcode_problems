#f"{low}->{high}

def summaryRanges(nums: list) -> list:
    if len(nums) == 0:
        return []
    
    low = nums[0]
    high = nums[0]
    ranges = []

    for i in range(0, len(nums)-1):
        if nums[i] +1 == nums[i+1]:
            high = nums[i+1]
        elif nums[i] +1 != nums[i+1]:
            if low == high:
                ranges.append(str(nums[i]))
                low = nums[i+1]
                high = nums[i+1]
            else:
                ranges.append(f"{low}->{high}")
                low = nums[i+1]
                high = nums[i+1]
        
    if low == high:
        ranges.append(str(high))
    else:
        ranges.append(f"{low}->{high}")
    return ranges


print(summaryRanges([0,2,3,4,6,8,9]))