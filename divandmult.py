def gen_array(d, k):
    array_d_k = []
    for i in range(d, k+1, d):
        array_d_k.append(i)
    return array_d_k

def gcd(x, y):
    if x >= y:
        while x % y != 0:
            temp = x % y
            x = y
            y = temp
        return y
    else:
        return gcd(y, x)


def lcm(x, y):
    return (x * y) / gcd(x, y)

def find_nums(d, k):
    array_of_pairs = []
    for i in gen_array(d, k):
        for j in gen_array(d, k):
            if gcd(i, j) == d and lcm(i, j) == k and not (j, i) in array_of_pairs:
                array_of_pairs.append((i, j))
    return array_of_pairs
