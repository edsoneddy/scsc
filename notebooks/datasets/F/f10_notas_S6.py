# read n lines with a name and a score
def read_students(n):
    students = []
    for _ in range(n):
        name, score = input().split()
        students.append((name, int(score)))
    return students

# grade thresholds: A >= 90, B >= 80, C >= 70, D >= 60, otherwise F
def classify(score):
    if 60 <= score and score < 70:
        return "D"
    elif 70 <= score and score < 80:
        return "C"
    elif 80 <= score and score < 90:
        return "B"
    elif 90 <= score and score <= 100:
        return "A"
    else:
        return "F"

# bubble sort: higher score first, ties by name
def rank(students):
    ordered = list(students)
    n = len(ordered)
    for i in range(n):
        for j in range(0, n - 1 - i):
            if ordered[j][1] < ordered[j + 1][1] or (ordered[j + 1][1] == ordered[j][1] and ordered[j][0] > ordered[j + 1][0]):
                ordered[j], ordered[j + 1] = ordered[j + 1], ordered[j]
    return ordered

def main():
    n = int(input())
    ordered = rank(read_students(n))
    total = 0
    position = 1
    for name, score in ordered:
        letter = classify(score)
        total = score + total
        print("%d %s %d %s" % (position, name, score, letter))
        position = position + 1
    if n > 0:
        average = total / n
    else:
        average = 0
    passed = i = 0
    while i < len(ordered):
        if ordered[i][1] >= 60:
            passed = passed + 1
        i = i + 1
    print(f"average {round(average, 2)} passed {passed} of {n}")

main()
