# read n lines with a name and a score
def read_students(n):
    students = []
    for _ in range(n):
        name, score = input().split()
        students.append((name, int(score)))
    return students

# grade thresholds: A >= 90, B >= 80, C >= 70, D >= 60, otherwise F
def classify(score):
    if score >= 90 and score <= 100:
        return "A"
    elif score >= 80 and score < 90:
        return "B"
    elif score >= 70 and score < 80:
        return "C"
    elif score >= 60 and score < 70:
        return "D"
    else:
        return "F"

# bubble sort: higher score first, ties by name
def rank(students):
    ordered = list(students)
    n = len(ordered)
    for i in range(n):
        for j in range(0, n - i - 1):
            if ordered[j][1] < ordered[j + 1][1] or (ordered[j][1] == ordered[j + 1][1] and ordered[j][0] > ordered[j + 1][0]):
                ordered[j], ordered[j + 1] = ordered[j + 1], ordered[j]
    return ordered

def main():
    n = int(input())
    ordered = rank(read_students(n))
    total = 0
    position = 1
    for name, score in ordered:
        letter = classify(score)
        total = total + score
        print(position, name, score, letter)
        position = position + 1
    if n > 0:
        average = total / n
    else:
        average = 0
    passed = i = 0
    while i < len(ordered):
        if not ordered[i][1] < 60:
            passed = passed + 1
        i = i + 1
    print("average", round(average, 2), "passed", passed, "of", n)

main()
