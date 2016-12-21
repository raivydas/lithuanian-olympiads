import copy

def get_representation(num):
    digits_array = []
    while num != 0:
        digits_array.append(num % 10)
        num /= 10
    return digits_array

def reconstruct_num(digits_array):
    num = 0
    order = 1
    for i in digits_array:
        num += order * i
        order *= 10
    return num

def switch_nums(i, j, digits_array):
    new_digits_array = copy.deepcopy(digits_array)
    temp = new_digits_array[i]
    new_digits_array[i] = new_digits_array[j]
    new_digits_array[j] = temp
    return new_digits_array

def find_largest_num(num):
    digits_array = get_representation(num)
    max_num = num
    for i in range(len(digits_array)):
        for j in range(len(digits_array)):
            new_digits_array = switch_nums(i, j, digits_array)
            new_num = reconstruct_num(new_digits_array)
            if new_num > max_num:
                max_num = new_num
    return max_num
