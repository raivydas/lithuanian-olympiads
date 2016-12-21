def two_lesser(num, nums):
    lesser_num = 0
    for i in nums:
        if i < num:
            lesser_num += 1
    if lesser_num == 2:
        return True
    else:
        return False

def two_greater(num, nums):
    greater_nums = 0
    for i in nums:
        if i > num:
            greater_nums += 1
    if greater_nums == 2:
        return True
    else:
        return False

def remove_el(i, nums):
    new_nums = nums[:]
    num = new_nums.pop(i)
    return (num, new_nums)

def determine(nums):
    for i in range(5):
        (num, new_nums) = remove_el(i, nums)
        if two_lesser(num, new_nums) and two_greater(num, new_nums):
            return True
    return False