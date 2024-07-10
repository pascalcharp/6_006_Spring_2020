def _search_id_in(v, n, lo, hi):
    if lo > hi:
        return hi
    mid = (lo + hi) // 2
    print(f"_search_id_in(v, {n}, {lo}, {hi}) = {mid}")
    if v[mid] > n:
        return _search_id_in(v, n, lo, mid - 1)
    elif v[mid] < n:
        return _search_id_in(v, n, mid + 1, hi)
    elif v[mid] == n:
        return mid


def _search_id(v, n):
    if n < v[0]:
        return -1
    return _search_id_in(v, n, 0, len(v) - 1)


if __name__ == '__main__':
    A = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(len(A)):
        assert i == _search_id(A, A[i])
        assert i == _search_id(A, A[i] + 0.5)

    print(_search_id(A, -1))
