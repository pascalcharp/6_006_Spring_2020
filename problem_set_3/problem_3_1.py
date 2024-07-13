from lib.hash_map import HashMap

def hash_function(n):
    return 11 * n + 4

if __name__ == '__main__':
    myTable = HashMap(hash_function, 9)
    keys = [67, 13, 49, 24, 40, 33, 58]
    for key in keys:
        myTable.insert(key, None)
    print(myTable)