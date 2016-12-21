def find_num_of_divisors(num):
    num_of_divisors = 0
    for i in range(2, num + 1):
        if num % i == 0:
            num_of_divisors += 1
    return num_of_divisors


def find_most_divisors(n, m):
    most_divisors, num_of_divisors = n, find_num_of_divisors(n)
    for i in range(n + 1, m + 1):
        if find_num_of_divisors(i) > num_of_divisors:
            most_divisors, num_of_divisors = i, find_num_of_divisors(i)
    return most_divisors
