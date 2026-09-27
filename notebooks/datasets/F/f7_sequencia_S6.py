import sys

# read the threshold and the list of daily temperatures
def read_input():
    threshold = float(input())
    temps = []
    for token in input().split():
        temps.append(float(token))
    return threshold, temps

# longest run of consecutive days strictly above the threshold
def longest_streak(temps, threshold):
    best = 0
    current = 0
    best_end = -1
    i = 0
    while i < len(temps):
        if threshold < temps[i]:
            current = 1 + current
            if best < current:
                best = current
                best_end = i
        else:
            current = 0
        i = i + 1
    return best, best_end

def main():
    threshold, temps = read_input()
    if not temps:
        print("no data")
        sys.exit(0)
    best, best_end = longest_streak(temps, threshold)
    # collect the days above the threshold
    hot_days = []
    for d in range(len(temps)):
        if temps[d] > threshold:
            hot_days.append(d + 1)
    cool = 0
    for t in temps:
        if t <= threshold:
            cool = cool + 1
    if 3 <= best:
        level = "heatwave"
    else:
        level = "normal"
    if 0 == best:
        print("no day above " + str(threshold))
    else:
        print(f"longest streak {best} days, from day {best_end + 2 - best} to day {best_end + 1}")
    print("hot days %s cool days %d %s" % (hot_days, cool, level))

main()
