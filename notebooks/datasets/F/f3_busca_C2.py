import bisect

# iterative binary search, returns an index or -1
def find_index(arr, key):
    lo = 0
    hi = len(arr) - 1
    while lo <= hi:
        middle = (lo + hi) // 2
        if arr[middle] == key:
            return middle
        elif arr[middle] < key:
            lo = middle + 1
        else:
            hi = middle - 1
    return -1

# first position where target could be inserted
def first_pos(arr, key):
    lo, hi = 0, len(arr)
    while lo < hi:
        middle = (lo + hi) // 2
        if arr[middle] < key:
            lo = middle + 1
        else:
            hi = middle
    return lo

# copies of the target = distance between the bounds of target and target + 1
def copies(arr, key):
    return first_pos(arr, key + 1) - first_pos(arr, key)

def run():
    arr = []
    for piece in input().split():
        arr.append(int(piece))
    arr.sort()
    qn = int(input())
    grand = 0
    for step in range(qn):
        key = int(input())
        where = find_index(arr, key)
        num = copies(arr, key)
        if bisect.bisect_left(arr, key) == first_pos(arr, key):
            verdict = "ok"
        else:
            verdict = "bad"
        if not where == -1 and num > 0:
            print(key, "found", num, "check", verdict)
        else:
            print(key, "missing", "check", verdict)
        grand = grand + num
    print("total matches", grand)

run()
