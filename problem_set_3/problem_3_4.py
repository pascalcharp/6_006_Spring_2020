from lib.hash_map import HashMap
from lib.hash_map_utilities import simple_integer_hash
from lib.radix_sort import radix_sort


def exact_sum_find(h, availables):
    map = HashMap(simple_integer_hash)
    for size in availables:
        map.insert(size, size)
    for size in availables:
        diff = h - size
        try:
            found = map.find(diff)
        except KeyError:
            pass
        else:
            return size, found
    return None


def find_lower_sum(h, s):
    index_list = radix_sort(s, 10)
    best = 0
    best_lo = -1
    best_hi = -1
    lo = 0
    hi = len(s) - 1
    while lo < hi:
        somme = index_list[lo] + index_list[hi]
        if somme < h:
            if somme > best:
                best = somme
                best_lo = lo
                best_hi = hi
            lo += 1
        elif somme > h:
            hi -= 1
        else:
            return index_list[lo], index_list[hi], best
    return index_list[best_lo], index_list[best_hi], best


if __name__ == '__main__':
    A = [10, 15, 12, 32, 78, 154, 110]
    print(exact_sum_find(44, A))
    print(find_lower_sum(94, A))
