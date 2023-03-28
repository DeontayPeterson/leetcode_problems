
test1 = [0,1,0,3,12] # -> [1,3,12,0,0]
t2 = [0,0,1]

def moveZeros(nums: list) -> None:
    index = 0

    for num in nums:
        if num != 0:
            nums[index] = num
            index += 1
            print(index)
    # for i in range(index, len(nums)):
    #     nums[i]= 0
    print(nums)
moveZeros(test1)
