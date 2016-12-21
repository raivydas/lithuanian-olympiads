def triangle(a, b, c):
    if a + b > c and a + c > b and c + b > a:
        return True
    else:
        return False

def partition_not_triangle(partition):
    for i in range(0, len(partition)):
        for j in range(i+1, len(partition)):
            for k in range(j+1, len(partition)):
                if triangle(partition[i], partition[j], partition[k]):
                    return False
    return True