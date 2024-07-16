import math


def radix_sort(A, radix):
    result = A
    max_value = max(A)
    max_power = math.log(max_value, radix)
    curr_power = 0
    curr_divisor = 1
    while curr_power <= max_power:
        queues = [[] for _ in range(radix)]
        for e in result:
            queues[(e // curr_divisor) % radix].append(e)
        result = []
        for q in queues:
            while q:
                result.append(q.pop(0))
        curr_power += 1
        curr_divisor *= radix
    return result

if __name__ == '__main__':
    A = [4, 1, 8, 2, 900, 432, 1, 923, 1796, 2746, 9325, 24]
    print(radix_sort(A, 10))