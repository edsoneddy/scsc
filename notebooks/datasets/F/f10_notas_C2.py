# read n lines with a name and a score
def load(size):
    pupils = []
    for _ in range(size):
        who, pts = input().split()
        pupils.append((who, int(pts)))
    return pupils

# grade thresholds: A >= 90, B >= 80, C >= 70, D >= 60, otherwise F
def grade_of(pts):
    if pts >= 90 and pts <= 100:
        return "A"
    elif pts >= 80 and pts < 90:
        return "B"
    elif pts >= 70 and pts < 80:
        return "C"
    elif pts >= 60 and pts < 70:
        return "D"
    else:
        return "F"

# bubble sort: higher score first, ties by name
def sort_by_score(pupils):
    lst = list(pupils)
    size = len(lst)
    for a in range(size):
        for b in range(0, size - a - 1):
            if lst[b][1] < lst[b + 1][1] or (lst[b][1] == lst[b + 1][1] and lst[b][0] > lst[b + 1][0]):
                lst[b], lst[b + 1] = lst[b + 1], lst[b]
    return lst

def run():
    size = int(input())
    lst = sort_by_score(load(size))
    acc = 0
    place = 1
    for who, pts in lst:
        grade = grade_of(pts)
        acc = acc + pts
        print(place, who, pts, grade)
        place = place + 1
    if size > 0:
        mean = acc / size
    else:
        mean = 0
    ok_n = a = 0
    while a < len(lst):
        if not lst[a][1] < 60:
            ok_n = ok_n + 1
        a = a + 1
    print("average", round(mean, 2), "passed", ok_n, "of", size)

run()
