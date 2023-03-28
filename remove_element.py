'''
0 <= nums.length <= 100 
0 <= nums[i] <= 50
0 <= val <= 100
'''

#1: The array COULD BE EMPTY.
#2: The elements in the array are from 0-50
#3: the Value to remove are from 0-100


list1 = [3,2,2,3]
val1 = 3
list2 = [0,1,2,2,3,0,4,2]
val2 = 2

t3 = [0,1,2,2,3,0,4,2] #-> [0,1,4,0,3] THE FIRST FIVE ELEMENTS CAN BE RETURNED IN ANY ORDER!
v3 = 2


def removeElement(nums: list, val: int) -> int:
    val_count = 0
    print(nums)


    for i in range(len(nums)):
        if nums[i] == val:
            print(f"{nums[i]} is equal to val!\n")
            val_count += 1
        else:
            if val_count != 0:
                nums[i - val_count] = nums[i] 
    print(nums)
    return len(nums) - val_count

print(removeElement(list2, val2))

