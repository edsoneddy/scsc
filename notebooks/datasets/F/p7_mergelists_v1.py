def merge_sorted(a, b):
    result = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result

list_a = list(map(int, input().split()))
list_b = list(map(int, input().split()))
merged = merge_sorted(list_a, list_b)
print(' '.join(map(str, merged)))
