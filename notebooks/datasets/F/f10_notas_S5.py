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
    else:
        if score >= 80 and score < 90:
            return "B"
        else:
            if score >= 70 and score < 80:
                return "C"
            else:
                if score >= 60 and score < 70:
                    return "D"
                else:
                    return "F"

# bubble sort: higher score first, ties by name
def rank(students):
    ordered = list(students)
    n = len(ordered)
    for i in range(n):
        for j in range(n - i - 1):
            if ordered[j][1] < ordered[j + 1][1] or (ordered[j][1] == ordered[j + 1][1] and ordered[j][0] > ordered[j + 1][0]):
                temp = ordered[j]
                ordered[j] = ordered[j + 1]
                ordered[j + 1] = temp
    return ordered

def main():
    n = int(input())
    ordered = rank(read_students(n))
    total = 0
    position = 1
    for name, score in ordered:
        letter = classify(score)
        total += score
        print(position, name, score, letter)
        position += 1
    average = total / n if n > 0 else 0
    passed = 0
    for i in range(len(ordered)):
        if not ordered[i][1] < 60:
            passed += 1
    print("average", round(average, 2), "passed", passed, "of", n)

main()
